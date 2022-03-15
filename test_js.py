from selenium import webdriver
class TestJs():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def test_js(self):
        self.driver.get('https://www.baidu.com/')

        # 执行js代码块的方式定位
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selelel')
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[2]').click()

        # 循环执行代码块
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))