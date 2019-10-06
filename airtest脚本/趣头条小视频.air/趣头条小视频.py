# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import datetime
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
    y1 = int(l[1] * 0.8)  #起始y坐标
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

file = r'D:\趣头条小视频.log'
f = open(file, 'a+')
start = datetime.datetime.now()

lmovie = poco(name='com.jifen.qukan:id/nr',text='小视频')
if(lmovie.exists()):
    lmovie.click()
    sleep(10)
    # 查看次数
    watch_num = 1
    while(True):
        sleep(10 +random.randint(0,10))
        swipeUp(1000,0.1)

        # 根据时间判断 两个小时结束
        cur = datetime.datetime.now()
        timeStyle=cur.strftime("%Y-%m-%d %H:%M:%S")
        strlog = '查看一个趣头条小视频，已看%d个' % watch_num
        strlog =strlog +timeStyle+'\n'
        f.write(strlog)
        print(strlog)
        watch_num += 1
        f.flush()
        if((cur-start).seconds >= 3600*2):
            break
else:
    f.write("小视频按钮不存在" + '\n')

f.close()
stop_app("com.jifen.qukan")
