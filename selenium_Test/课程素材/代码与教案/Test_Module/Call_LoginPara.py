from selenium import webdriver
from LoginClass_para import *
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)

Login().user_login(driver,'51zxw',123456)
sleep(3)
Login().user_logout(driver)

Login().user_login(driver,'51zxwPro',123456)
sleep(3)
Login().user_logout(driver)

sleep(3)
driver.quit()