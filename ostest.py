# class h:
#     def s(self):
#         print("123")
#     def t(self):
#         self.s()
#
# zihan = h()
# zihan.t()
#
#
# a= 1
# b =2
# a,b = b,a
#
#
# # s = [1,2,3,4,5,6]
# # print(s[1:4:2])
# [print(i*3) for i in range(1,4)]
#
# list_a = [1,2,3]
# list_a.extend([4,5])
# print(list_a)
#
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d.values())
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# class TestWait:
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://www.baidu.com")
#     def test_wait(self):
#         self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('123')

    # def test_wait(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="kw"]').click()
# def test():
#     driver = webdriver.Chrome()
#     driver.get("www.baidu.com")




from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
import time

from selenium.webdriver.common.keys import Keys


class TestA:
    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # 点击、右键点击、双击
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()
        time.sleep(6)

    # 移动光标到
    @pytest.mark.skip
    def test_move_to(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(6)

    # 拖拽元素到指定位置
    @pytest.mark.skip
    def test_drop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag = self.driver.find_element_by_id('dragger')
        drop = self.driver.find_element_by_xpath('/html/body/div[3]')
        drop2 = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)

        # 拖拽元素到指定位置的三种方法
        action.drag_and_drop(drag, drop)
        action.drag_and_drop(drag, drop2)
        # action.click_and_hold(drag).release(drop)
        # action.click_and_hold(drag).move_to_element(drop).release()

        action.perform()
        time.sleep(6)


    # 输出操作
    @pytest.mark.skip
    def test_key(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input').click()
        action = ActionChains(self.driver)
        action.send_keys("王子函 真聪明")
        time.sleep(2)
        action.send_keys(Keys.BACK_SPACE)  #删除键
        action.perform()
        time.sleep(5)

    def test_touchaction(self):
        self.driver.get("https://www.baidu.com/")
        # time.sleep(5)
        ele = self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('软件测试')
        # time.sleep(5)
        han = self.driver.find_element_by_xpath('//*[@id="su"]').click()

        action = TouchActions(self.driver)
        action.tap(han)
        # time.sleep(5)
        action.scroll_from_element(ele, 0, 10000).perform()
        # action.perform()

        