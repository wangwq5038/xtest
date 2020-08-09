from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("#kw").send_keys("Selenium 我要自学网")
driver.find_element_by_css_selector(".s_ipt").send_keys("Selenium")
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("Python3")

sleep(2)
# driver.find_element_by_id("su").click()

driver.get("http://www.51zxw.net")
driver.find_element_by_css_selector("form#loginForm>ul>input[type='password']").send_keys('51zxw666')
sleep(2)
driver.quit()
