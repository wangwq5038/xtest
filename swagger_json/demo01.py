from selenium import webdriver

class TestKeyWords(object):
    #初始化
    def __init__(self,url,browser_type):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)
    #调用浏览器
    def open_browser(self,browser_type):
        if browser_type == 'Chrome':
            driver = webdriver.Chrome()
            return driver
        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
            return driver
        else:
            print('type error')
     # 元素定位       
    def locator(self,locator_type,value):
        if locator_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == 'name':
            el = self.driver.find_element_by_name(value)
            return el
    # def locator1(self,*value):
    #     return self.driver.find_element(value)
    # 输入
    def input_text(self,locator_type,value,text):
        self.locator(locator_type,value).send_keys(text)
    #点击
    def click_element(self,locator_type,value):
        self.locator(locator_type,value).click()
        
        
        
    



    


if __name__ == "__main__":
    tk = TestKeyWords('http://www.baidu.com','Chrome')
    tk.input_text('id','kw','selenium')
    tk.click_element('id','su')