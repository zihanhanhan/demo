import os
from selenium import webdriver


class Base:
    def setup(self):
        brower = os.getenv("brower")
        # if brower == 'firefox':
        #     self.driver = webdriver.firefox()
        # else:
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.firefox()

    def test_duo(self):
        self.driver.get('https://www.baidu.com/')