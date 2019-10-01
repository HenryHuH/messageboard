# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

import random

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#================================公用函数=======================
#自定义滑动事件
def getSize():
    s=poco.get_screen_size()
    return (s[0], s[1])
#屏幕向上滑动
def swipeUp(t,percent):
    l = getSize()
    x1 = int(l[0] * 0.5)+ random.randint(0,20) #x坐标
    y1 = int(l[1] * 0.7)  #起始y坐标
    y2 = int(l[1] * percent)   #终点y坐标

    swipe((x1, y1), (x1, y2),t+random.randint(0,20))
    
# =============================================================
# 趣头条app
# 先关闭视频app
stop_app("com.jifen.qukan")
# 开始阅读趣头条小视频        
start_app("com.jifen.qukan",activity=None)
# 进入小视频接口
# 等待15秒启动加载
sleep(20)
lmovie = poco(name='com.jifen.qukan:id/nr',text='小视频')
if(lmovie.exists()):
    lmovie.click()
    sleep(10)
    # 查看次数
    watch_num = 1
    while(watch_num<800):
        sleep(10 +random.randint(0,20))
        swipeUp(1000,0.3)
        print('趣头条查看一个视频，已看%d个' % watch_num)
        watch_num += 1

stop_app("com.jifen.qukan")