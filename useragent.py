import requests
#!/usr/bin/ python3
# -*- coding: utf-8 -*-
import requests
import datetime
import random
import json
import uuid
import time
import unicodedata
from selenium import webdriver
import os

class UserAgent(object):

    def init_proxy(self):
        self.proxies = self.get_proxy('f7a10ec3ecb94f4986b67b8ec37162ab', 'YZ20199151235oMhVE2')
        #self.deviceToken = str(uuid.uuid1())

    def get_proxy(self, xdl_spiderId, xdl_ddbh):
        url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=" + xdl_spiderId + "&orderno=" + xdl_ddbh + "&returnType=2&count=1"
        rece = requests.get(url)
        rece = rece.json()
        print(rece)
        port = rece['RESULT'][0]['port']
        ip = rece['RESULT'][0]['ip']
        proxy = ip + u"：" + port
        proxy = unicodedata.normalize('NFKC',proxy)
        print(u'当前IP:'+proxy)

        proxies = {
            "http": "http://" + proxy,
            "https": "https://" + proxy,
        }

        return proxies

    def get_html(self, url):

        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN",
            "Refer": "https://stock-account.superharvestwealth.com/?inviterCode=H0NHGC&name=",
            "Host": "stock-account.superharvestwealth.com",
            "Origin": "https://stock-account.superharvestwealth.com",
            "X-Requested-With": "com.tencent.mm"
        }
        # data = {
        #     'inviterCode': 'H0NHGC',
        #     'invokeType': '2',
        #     'reCode': '86',
        #     'mobile': iphone,
        #     'scode': verification,
        # }
        session = requests.Session()
        try:
            """模拟登陆获取cookie"""
            resp = session.post(
                url=url,
                headers=headers,
                data="",
                proxies=self.proxies
            )

            resp_dict = resp.json()

            if resp_dict["errorCode"] == 0:
                print("登陆成功")
                now = int(round(time.time() * 1000))
                now02 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))

                f = open('./fengshou.log', 'a')
                f.write(str(iphone) + '--mima110120--' + now02 + '\n')
                f.close()
                # 获取登陆过的cookies
                # cookies = resp.cookies
                # print(cookies)
            else:
                print("登陆失败")
        except BaseException as e:
            print("异常 登陆失败")
            print(resp)


if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

    chromedriver = "D:/AirtestIDE_2019-05-09_py3_win64/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options)
    driver.get("https://www.baidu.com/")  # 打开网址
    driver.maximize_window()  # 窗口最大化
    # driver.quit()

