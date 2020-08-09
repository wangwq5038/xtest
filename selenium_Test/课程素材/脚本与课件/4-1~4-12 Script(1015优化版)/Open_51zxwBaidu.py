from selenium import  webdriver
from time import sleep

driver=webdriver.Firefox()
# driver=webdriver.Chrome()
# driver=webdriver.Ie()

driver.get("http://www.51zxw.net")
print(driver.title)
sleep(3)

driver.get("http://www.baidu.com")
print(driver.title)
sleep(2)

# driver.quit()