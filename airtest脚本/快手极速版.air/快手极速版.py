
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

devs = device()
print(devs.list_app(third_only=True))

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

# ================================================
# 快手极速版
# 先关闭视频app
stop_app("com.kuaishou.nebula")
# 启动app 等待5秒
start_app("com.kuaishou.nebula",activity=None)
# 等待8秒启动加载
sleep(20)


# 1、左上角入口
flag=0
leftbtn = poco(name='com.kuaishou.nebula:id/left_btn',type='android.widget.ImageView')
if(leftbtn.exists()):
    leftbtn.click()
    sleep(8)
    mkmoney = poco(name ='com.kuaishou.nebula:id/red_packet_text',text='去赚钱')
    if(mkmoney.exists()):
        mkmoney.click()
        sleep(10)
        swipeUp(1000,0.3)
        sleep(8)
        seemovie =poco(name='android.view.View',text='去赚钱')
        if(seemovie.exists()):
            sleep(3)
            seemovie.click()
            flag =1
# 查看次数
watch_num = 1

if(flag==1):
    #开始看视频    
    while(watch_num<800):
        sleep(10 +random.randint(0,20))
        swipeUp(1000,0.3)
        print('查看一个快手极速视频，已看%d个' % watch_num)
        watch_num += 1

# 关闭视频app
stop_app("com.kuaishou.nebula")        
        

        