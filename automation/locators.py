from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//input[@name='name']").send_keys("hari")