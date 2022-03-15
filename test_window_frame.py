from selenium import webdriver
class Testwindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="s-top-loginbtn"]').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__regLink"]').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('2131312')
        # 切换 frame
        # 切换到指定结点
        self.driver.switch_to_frame()
        # 切换到父节点
        self.driver.switch_to.parent_frame()
        # 切换到默认的结点
        self.driver.switch_to.default_content()

