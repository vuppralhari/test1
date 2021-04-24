
from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://www.youtube.com/")

print(driver.title)

print(driver.current_url)

