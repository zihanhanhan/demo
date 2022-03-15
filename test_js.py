import pytest
import time
from selenium import webdriver
class TestJs():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    @pytest.mark.skip
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

        #依次执行代码块  只返回第一个return
        print(self.driver.execute_script('return document.title ; return JSON.stringify(performance.timing)'))

        # js处理 - 案例3 - 时间控件
        # 大部分时间控件都是readonly属性，需要手动去选择对应的时间，手工测试中很容易做到，自动化中对控件的操作可以使用js来操作。
        # 处理时间控件思路:
        # 1.要取消日期的readonly属
        # 2.给value赋值
        # 写js代码来实现如上的1，2点，再webdriver对js进行处理
    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("document.getElementById('train_date').value='2022-04-01'")
        time.sleep(3)