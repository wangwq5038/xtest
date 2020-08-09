from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_link_text("设置").click()
sleep(2)
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# driver.find_element_by_link_text("保存设置").click()
driver.find_element_by_link_text("恢复默认").click()

sleep(3)

driver.switch_to.alert().accept()

sleep(2)

driver.quit()