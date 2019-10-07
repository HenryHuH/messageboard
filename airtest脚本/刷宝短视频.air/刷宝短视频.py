# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import datetime
import random

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
devs = device()
print(devs.list_app(third_only=True))
#自定义滑动事件
def getSize():
    s=poco.get_screen_size()
    return (s[0], s[1])
#屏幕向上滑动
def swipeUp(t,percent):
    l = getSize()
    x1 = int(l[0] * 0.5)+ random.randint(0,20) #x坐标
    y1 = int(l[1] * 0.6)  #起始y坐标
    y2 = int(l[1] * percent)   #终点y坐标

    swipe((x1, y1), (x1, y2),t+random.randint(0,20))
    
# 刷宝短视频app
# 先关闭视频app
stop_app("com.jm.video")
# 开始阅读刷宝短视频       
start_app("com.jm.video",activity=None)
# 进入小视频接口
poco("com.jm.video:id/image_view")# 等待15秒启动加载
sleep(20)

file = r'D:\刷宝短视频.log'
f = open(file, 'a+')
start = datetime.datetime.now()

# 查看次数
watch_num = 1
while(True):
    sleep(8 +random.randint(0,10))
    swipeUp(1000,0.1)

    # 根据时间判断 两个小时结束
    cur = datetime.datetime.now()
    timeStyle=cur.strftime("%Y-%m-%d %H:%M:%S")
    strlog = '查看一个刷宝小视频，已看%d个' % watch_num
    strlog =strlog +timeStyle+'\n'
    f.write(strlog)
    print(strlog)
    watch_num += 1
    f.flush()
    if((cur-start).seconds >= 3600):
        break

f.close()
stop_app("com.jm.video")