from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

driver.get("https://admindev1.engagetoelect.com/login")
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element('xpath','//input[@class = "intro-x login__input form-control py-3 px-4 block"]').send_keys("vishnutest60@gmail.com")
driver.find_element("xpath",'//input[@class = "intro-x login__input form-control py-3 px-4 block mt-4"]').send_keys("password")
driver.find_element('id', "login_btn").click()
sleep(2)

driver.find_element('xpath','//div[contains(text(), "Citizens")]').click()
sleep(4)
driver.find_element('xpath','//div[contains(text() ,"Citizen Management")]').click()
sleep(4)


driver.find_element('xpath',"//a[@class ='btn btn-primary shadow-md mr-2 flex items-center']").click()
sleep(4)
driver.find_element('xpath',"//input[@id='aadhar_number']").send_keys(626753294991)
sleep(1)
driver.find_element("xpath",'//a[text()="Register Manually"]').click()
sleep(4)
driver.find_element('xpath','//input[@id ="username"]').send_keys('Prashanthi_pilai QA0624')
sleep(1)
driver.find_element('xpath','//input[@id ="password"]').send_keys('pass123')
sleep(1)
driver.find_element('xpath','//input[@id = "firstName"]').send_keys("Prashanthi")
sleep(1)
driver.find_element('xpath','//input[@id = "lastName"]').send_keys("Pilai")
sleep(1)
driver.find_element('xpath','//input[@id = "eamil"]').send_keys("Prashanthi.pilai@gmail.com")
sleep(5)

#list_box = driver.find_element('xpath','//select[@name = "gender"]')
#sleep(5)
#select = Select(list_box)
#sleep(5)
#select.select_by_visible_text("Female")
#sleep(5)


driver.find_element('xpath','//input[@id = "phoneNumber"]').send_keys(8088145149)
driver.find_element('xpath','//input[@id = "aadharNumber"]').send_keys(626753294991)
driver.find_element('xpath', '//textarea[@id = "address"]').send_keys("RR Nagar, Banglore")
driver.find_element('xpath','//input[@id = "districtSelect"]').send_keys("Banglore")
driver.find_element('xpath','//textarea[@id = "educationUG"]').send_keys("BE")
driver.find_element('xapth','//input[@id = "cityTown"]').send_keys("Banglore")
driver.find_element('xpath','//input[@id = "educationPG"]').send_keys("MTech")
driver.find_element('xpath','//input[@id = "pinCode"]').send_keys(530068)
driver.find_element('xpath','//input[@name = "profesionalExperience"]').send_keys("Engineer")
driver.find_element('xpath','//input[@name = "profesionalDepartment"]').send_keys("IT")
sleep(5)