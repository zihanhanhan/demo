from selenium import webdriver
import time
class TestFile:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_file(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_xpath('//*[@id="uploadImg"]').send_keys("E:\实验室\测试开发\gui秘钥.png")
        time.sleep(3)

    def test_alert(self):
        # 弹出框点击确认
        self.driver.switch_to_alert.accept()

        # 返回默认界面
        self.driver.switch_to_default_content()
'''
弹框处理机制
在页面操作中有时会遇到JavaScript所生成的alert、confirm以及prompt弹框，可以使用
switch_to.alert()方法定位到。然后使用text/ accept /dismiss/send_keys等方法进行操作。参考教你分辨alert、window、div模态框,以及操作
操作alert常用的方法:
 switch_to.alert():获取当前页面上的警告框。
144115232982625494正在观看视频
text:返回alert/confirm/ prompt中的文字信息。 accept():接受现有警告框。
 dismiss():解散现有警告框。
 send kevs(keysToSend):发送文本至警告框。keysToSend:将文本发送至警告框。
'''


