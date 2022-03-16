"""
复用浏览器
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 定义配置的实例对象option
option = Options()
# 修改实例属性 为 debug 模式启动的 ip +端口
option.debugger_address = "localhost:9222"
# 实例化driver时，添加option配置
driver = webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()

# 想要调试的步骤可以把前面的步骤注释掉，只执行新的步骤