import time

import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookies(self):
        # 1.访问企业微信主页/登陆页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2. 等待10s，人工扫码操作
        time.sleep(15)
        # 3.等待成功登录后获取cookie信息
        cookie = self.driver.get_cookies()
        # 4.将cookie存入一个可持久存储的地方、文件
        with open("cookie.yaml","w") as f:
            yaml.safe_dump(cookie, f)

    # def test_add_cookies(self):
    #     # 1.访问企业微信主页面
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     # 2.定义cookie，先手动粘贴，随后优化
    #     cookie = [
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
    #          'value': 'true'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
    #          'value': ''},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
    #          'value': '1688856691329322'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
    #          'value': '1970325473985207'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
    #          'value': '1688856691329322'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
    #          'value': 'direct'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
    #          'value': '1'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
    #          'value': '0126424'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
    #          'value': 'NbWmxrk5vj_-Hdt3Av0UaD8toC7qnc-oQARWa4QxP-Q9Kydm-NkB_mEvgAOU4-Ms'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1678983663.478286, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
    #          'path': '/', 'secure': False, 'value': '0'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
    #          'value': 'a7380480'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
    #          'value': '1Gh75eDQVYZplPJnqJwdI9no9s-2oQ8HizaVQBt1EsbBEBtcaQ8hAMWICQoHmzcLb4RXYuVyg-PKRFGoeAGjY2zkyzyxSpcLwfrjLQO-qik0rmyph2m06siPDRnIvM6Sa_uLaW1f3xXzV63T-NFY1wcA4TLbLe66v1AJeAfm6KKUv-zUoOVOQpwuU-1XMfGS_EmROo5yksb-n8xIogeTHlwybtJh7SrEPLB-bzL8Oyc6GVQETAd86JrQtKc9U5hckgtBTtcAEbyx4_XD1NHqLw'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1650039677.818326, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
    #          'path': '/', 'secure': False, 'value': 'zh'}]
    #     for c in cookie:
    #         self.driver.add_cookie(c)
    #     time.sleep(3)
    #     # 4.再次访问网页，发现无需扫码
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    def test_add_cookies(self):
        # 1.访问企业微信主页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2.找到写入的cookie文件
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3.植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问网页，发现无需扫码
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")