
# -*- encoding=utf8 -*-
__author__ = "Administrator"
import datetime
import schedule
import threading
import time
import os

# 三小时
def kuaishou():
    os.system("airtest run ./airtest脚本/快手极速版.air --device Android:///")

# 两小时
def qutoutiao():
    os.system("airtest run ./airtest脚本/趣头条小视频.air --device Android:///")

# 两小时
def dongfang():
    os.system("airtest run ./airtest脚本/东方头条.air --device Android:///")

# 两小时
def douyin():
    os.system("airtest run ./airtest脚本/抖音极速版.air --device Android:///")

def run():
    kuaishou()
    dongfang()
    douyin()
    qutoutiao()

if __name__ == "__main__":
    run()