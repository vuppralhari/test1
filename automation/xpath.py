from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://outlook.live.com/owa/")
driver.find_element_by_xpath("//a[@data-task='signin']").click()
driver.find_element_by_xpath("//input[@id='i0116']").send_keys("vuppralhari@outlook.com")
driver.find_element_by_xpath("//body[@class='cb']").click()
