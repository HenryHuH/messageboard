
# -*- encoding=utf8 -*-
__author__ = "Administrator"
import datetime
import schedule
import threading
import time
import os

def kuaishou():
    os.system("airtest run ./airtest脚本/快手极速版.air --device Android:///")

def qutoutiao():
    os.system("airtest run ./airtest脚本/趣头条小视频.air --device Android:///")


def dongfang():
    os.system("airtest run ./airtest脚本/东方头条.air --device Android:///")

def douyin():
    os.system("airtest run ./airtest脚本/抖音极速版.air --device Android:///")

def shuabao():
    os.system("airtest run ./airtest脚本/刷宝短视频.air --device Android:///")
def run():

    while(True):

        kuaishou()
        shuabao()
        dongfang()
        qutoutiao()
        douyin()


if __name__ == "__main__":
    run()