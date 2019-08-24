from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\AJAY\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\selenium\\chromedriver.exe')
driver.set_page_load_timeout(30)
driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.implicitly_wait(20)

drive
