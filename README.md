# Selenium - Web Scraping

จากเว็บไซน์ Wongnai ทางผู้เขียนต้องการดึงข้อมูล 20 ร้านอาหารที่ได้รับ Users’ Choice 2024 โซนร้านอาหารอารีย์ จตุจักร ลาดพร้าว และกรุงเทพฯตอนบน โดยจะใช้ Library Selenium ใน Python แล้วจะจัดเก็บข้อมูลลงสู่ Database

![Flow](https://github.com/suben-mk/Selenium-Web-Scraping/assets/89971741/1ba549cc-417b-4a8c-98eb-395e9056ea3f)\
_Web Scraping Flow_

![image](https://github.com/suben-mk/Selenium-Web-Scraping/assets/89971741/ac629f1a-5bd9-42fe-9a7d-32547ea79f31)
_Wongnai : Users’ Choice 2024 โซนร้านอาหารอารีย์ - จตุจักร - ลาดพร้าว - กรุงเทพฯ ตอนบน_

## Workflow
_**Python libraries :**_ _Selenium, Pandas, SQLAlchemy_\
Python script และ process ทั้งหมด [Selenium-LINE_MAN_Wongnai_Users_Choice_2024.py](https://github.com/suben-mk/Selenium-Web-Scraping/blob/main/Selenium-LINE_MAN_Wongnai_Users_Choice_2024.py)

![image](https://github.com/suben-mk/Selenium-Web-Scraping/assets/89971741/12e8a782-c8d4-4a12-8659-7e459ef6a9fb)
_Scraping Data_

## Output
ผลลัพธ์ที่ได้จากการดึงข้อมูล รูปแบบไฟล์ database [LineManWongnaiUsersChoice2024.db](https://github.com/suben-mk/Selenium-Web-Scraping/blob/main/LineManWongnaiUsersChoice2024.db)

**20 ร้านอาหารที่ได้รับ Users’ Choice 2024 โซนร้านอาหารอารีย์ จตุจักร ลาดพร้าว และกรุงเทพฯตอนบน**
No	|	Name	|	Category	|	Address	|	Recommend	|	Rate	|	Review
-------	|	-------	|	-------	|	-------	|	-------	|	-------	|	-------
1	|	จันทน์หอม รามคำแหง21	|	อาหารใต้ , อาหารไทย	|	273/4 ซอย รามคำแหง 21 กรุงเทพมหานคร	|	ยอดเหลียงผัดไข่, แกงเหลืองปลากระพง, หมูโค	|	4	|	274
2	|	Nana Coffee Roasters	|	ร้านกาแฟ/ชา , คาเฟ่	|	24/2 ซอย อารีย์ 4 กรุงเทพมหานคร	|	Dirty, Wake Up, Iced Latte	|	4.2	|	162
3	|	Cast Iron Burgerhaus	|	เบอร์เกอร์ , กึ่งผับ/ร้านเหล้า/บาร์ , อาหารอเมริกัน	|	2/7, ซอยพหลโยธิน 7, สามเสนใน, กรุงเทพมหานคร, 10400, ประเทศไทย กรุงเทพมหานคร	|	เบค่อนชีสเบอร์เกอร์, สวิสมัชรูม, ชังค์กี้บลูชีส	|	4.2	|	159
4	|	หมูกรอบนายไซ	|	อาหารไทย , อาหารจานเดียว , อาหารจีน	|	1059, ประชาชื่น วงศ์สว่าง บางซื่อ กรุงเทพมหานคร กรุงเทพมหานคร	|	ข้าวหมูกรอบ พิเศษ, หมูกรอบ ขีดละ, ข้าวหมูกรอบ+หมูแดง พิเศษ	|	4	|	424
5	|	บ้านพึงชม	|	อาหารไทย	|	38/1, ซอยเจือจิตร กรุงเทพมหานคร	|	วุ้นเส้นผัดสามเหม็น, เนื้อทอดคุณหมี, ใบเหลียงผัดไข่	|	4	|	217
6	|	Barney's Burger Joint	|	เบอร์เกอร์	|	404, ซอย เข้าตึกพหลโยธินเซ็นเตอร์ ร้านอยู่ในสุดซ้ายมือครับ (ซอยข้างตึกพหลโยธินเพลสปากซอยมี7-11) ซอยที่เค้าขายของกันครับ สามเสนใน พญาไท กรุงเทพมหานคร กรุงเทพมหานคร	|	American trucker, Trucker (Double) beef, ชีสเบอร์เกอร์	|	4.6	|	66
7	|	ครูสายฐิพย์-ข้าว ยำ ธรรม แกง	|	อาหารไทย , คาเฟ่	|	6-7 ถนน นาคนิวาส เขตลาดพร้าว กรุงเทพมหานคร 10230 กรุงเทพมหานคร	|	ใบเหลียงผัดไข่กุ้งเสียบ, หมูทอดเกลือ, ผักกูดต้มกะทิกุ้ง	|	4.2	|	83
8	|	Chocolate Ville	|	อาหารไทย , อาหารกล่อง/ข้าวกล่อง เดลิเวอรี , อาหารตามสั่ง	|	รามอินทรา, ประเสริฐมนูกิจ รามอินทรา คันนายาว กรุงเทพมหานคร กรุงเทพมหานคร	|	ขาหมูเยอรมัน, แซลมอนแซ่บ, พิซซ่าแฮมเห็ด	|	4.1	|	662
9	|	Ohachi Butadon (สาขาอารีย์)	|	อาหารญี่ปุ่น , ปิ้งย่าง	|	1251, โครงการสนั่นนภา ชั้น 2 เลขที่ 1251 ซอยพหลโยธิน 7 สามเสนใน พญาไท กรุงเทพมหานคร กรุงเทพมหานคร	|	ไข่ออนเซ็น, บูตะดง มาสเตอร์ Master, บูตะดง มาตรฐาน Regular	|	4.3	|	161
10	|	KENNY'S BKK	|	พิซซ่า , เบอร์เกอร์ , อาหารอิตาเลียน	|	12, พหลโยธิน ซอย5 สามเสนใน พญาไท กรุงเทพมหานคร กรุงเทพมหานคร	|	THE RUMBLE, Salt and pepper grilled calamari, CORN RIBS	|	4.5	|	31
11	|	เผ็ด เผ็ด คาเฟ่ (phed phed cafe)	|	อาหารอีสาน/ร้านส้มตำ , อาหารไทย	|	9 ซอย ประดิพัทธิ์ 20 แขวง สามเสนใน เขตพญาไท กรุงเทพมหานคร 10400 ประเทศไทย กรุงเทพมหานคร	|	ข้าวผัดเบคอนกากหมู, กากหมู, น้ำลำไย	|	4.2	|	145
12	|	อบอร่อย ทาวน์อินทาวน์ (ไม่มีสาขา)	|	อาหารทะเล	|	1329/53, ศรีวรา พลับพลา วังทองหลาง กรุงเทพมหานคร กรุงเทพมหานคร	|	กุ้งอบวุ้นเส้น, หอยเชลล์อบเนย, ข้าวผัดปูใหญ่	|	4.2	|	174
13	|	ขมิ้น Camin Cuisine & Cafe	|	อาหารใต้ , คาเฟ่ , อาหารไทย	|	ประเสริฐมนูกิจ 2 กรุงเทพมหานคร	|	แกงส้มปลากระพง, หมูฮ้อง, ใบเหลียงผัดไข่	|	4.3	|	144
14	|	SOUSAKU อารีย์	|	อาหารญี่ปุ่น	|	39/1, ซอยอารีย์ 4 สามเสนใน พญาไท กรุงเทพมหานคร กรุงเทพมหานคร	|	Crispy Salmon Skin Roll, Gyu (beef) signature set, Buta (pork) signature set	|	4.1	|	264
15	|	โอว ก๋วยเตี๋ยวพริกสด	|	ก๋วยเตี๋ยว , อาหารจานเดียว , อาหารจีน	|	91, ซอยรามอินทรา 14 ท่าแร้ง บางเขน กรุงเทพมหานคร กรุงเทพมหานคร	|	ก๋วยเตี๋ยวทะเลพริกสด, ลูกชิ้นกุ้งทอด ชุดละ, เกี๊ยวกุ้งลวกจิ้ม	|	4	|	313
16	|	ใจดี Shrimp	|	อาหารใต้ , อาหารไทย	|	222/388 หมู่บ้านโนเบิ้ล จีโอ ถ.ร่วมมิตรพัฒนา ซ.วัชรพล แขวงท่าแร้ง เขตบางเขน กรุงเทพมหานคร 10220 กรุงเทพมหานคร	|	แกงเหลืองปลากะพงยอดมะพร้าว, ใบเหลียงผัดไข่, คั่วกลิ้งกุ้งสับ	|	4.2	|	117
17	|	นาย ต. เนื้อตุ๋น วัชรพล	|	ก๋วยเตี๋ยว	|	91/30, วัชรพล ท่าแร้ง บางเขน กรุงเทพมหานคร กรุงเทพมหานคร	|	หม้อไฟ, เกาเหลาเนื้อ(พิเศษ), ก๋วยเตี๋ยวเนื้อ(พิเศษ)	|	4.2	|	147
18	|	ครัวสา รสจัด	|	อาหารไทย	|	112/1, วิภาวดี-รังสิต ลาดยาว จตุจักร กรุงเทพมหานคร กรุงเทพมหานคร	|	หมูสะเต๊ะ จานเล็ก, หอยแครงดิสโก้, กุ้งแม่น้ำฉู่ฉี่	|	4.2	|	390
19	|	หมีแฟมิลี่ me & family	|	ชาบู/สุกี้ยากี้/หม้อไฟ	|	ซอยเสริมสุขแยก 1, จตุจักร, กรุงเทพมหานคร, 10900, ประเทศไทย กรุงเทพมหานคร	|	หมูกรอบเพลย์ยาร์ด, เต้าหู้เหลืองทอด, ชุดแฟมิลี่หมู(ไม่มีผัก)	|	4.2	|	154
20	|	Sushi Ichizu	|	ซูชิ , อาหารญี่ปุ่น	|	1972, ถนนเพชรบุรี, บางกะปิ, กรุงเทพมหานคร, 10310, ประเทศไทย กรุงเทพมหานคร	|	Chirashi box	|	4.6	|	70
