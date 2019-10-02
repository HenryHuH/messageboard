
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

def run():

    schedule.every().day.at("00:26").do(kuaishou)

    schedule.every().day.at("04:40").do(qutoutiao)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run()