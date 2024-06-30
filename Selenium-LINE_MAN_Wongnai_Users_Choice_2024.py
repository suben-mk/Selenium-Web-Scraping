# Import module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from sqlalchemy import create_engine

# Function of scraping website Wongnai
def scrapWongnai(url):
    # Open website Wongnai Users' Choice 2024
    url_uc2024 = url
    driver.get(url_uc2024)
    time.sleep(5) # delay

    # Dataframe of Wongnai Users' Choice 2024
    df_uc2024 = pd.DataFrame(columns=['No', 'Name', 'Category', 'Address', 'Recommend', 'Rate', 'Review'])

    # Scraping content data from wabsite
    uc2024_data = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]')
    time.sleep(5) # delay

    # List of 20 LINE MAN Wongnai Users’ Choice 2024
    for r in uc2024_data:
        try:
            for i in range(1, 21):
                no = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div/div[1]/a/div/span').text
                name = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/a/h5').text
                category = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/div[6]').text.split('ร้านอาหารประเภท ')  
                address = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/div[5]').text
                recommend = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/div[3]/div').text.split('เมนูเด็ด: ')
                rate = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/div[1]/div/div/div[1]/div/div/div').text
                review = r.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div[1]/div[2]/div[1]/div/div/span').text.split(' รีวิว')

                df_uc2024 = df_uc2024._append({'No' : no, 'Name' : name, 'Category' : category[1], 'Address' : address, 'Recommend' : recommend[1], 'Rate' : rate, 'Review' : review[0]}, ignore_index=True)
                time.sleep(1) # delay
        except:
            break
    time.sleep(5) # delay
    return df_uc2024

# Path chrome driver
chrome_driver_path = r'C:\Users\SUBEN\OneDrive\Desktop\Web Scraping Project - LINE MAN Wongnai Users Choice 2024\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Website Wongnai Users' Choice 2024 ; ร้านอาหารอารีย์ - จตุจักร - ลาดพร้าว - กรุงเทพฯ ตอนบน
url_wongnai = 'https://www.wongnai.com/collections/line-man-wongnai-users-choice-2024-%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%AD%E0%B8%B2%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B9%8C-%E0%B8%88%E0%B8%95%E0%B8%B8%E0%B8%88%E0%B8%B1%E0%B8%81%E0%B8%A3-%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B8%9E%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%A7-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%AF-%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%9A%E0%B8%99'

# Scraping website Wongnai
LMWN_UC2024 = scrapWongnai(url_wongnai)

# Close all working webdriver
time.sleep(5) # delay
driver.quit()

# Load to database (SQLite)
engine = create_engine('sqlite:///LineManWongnaiUsersChoice2024.db') # Turn on database engine
LMWN_UC2024.to_sql('LMWN_UC2024', index=False, if_exists='replace', con=engine)