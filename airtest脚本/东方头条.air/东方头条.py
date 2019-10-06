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
    y1 = int(l[1] * 1.0)  #起始y坐标
    y2 = int(l[1] * percent)   #终点y坐标

    swipe((x1, y1), (x1, y2),t+random.randint(0,20))
    
# =============================================================
# 东方头条app
# 先关闭视频app
stop_app("com.songheng.eastnews")
# 开始阅读趣头条小视频        
start_app("com.songheng.eastnews",activity=None)
# 进入小视频接口
# 等待15秒启动加载
sleep(20)

file = r'D:\东方头条.log'
f = open(file, 'w+')
start = datetime.datetime.now()

movie = poco(name='com.songheng.eastnews:id/ab3',text='视频')
if(movie.exists()):
    movie.click()
    sleep(10)
    lmovie = poco(name='android.widget.TextView',text='小视频')
    if(lmovie.exists()):
        lmovie.click()
        sleep(5)
        ll = poco(name ='com.songheng.eastnews:id/sw',type ='android.widget.ImageView')
        if(ll.exists()):
            ll.click()
            sleep(8)
            # 开始刷小视频
            # 查看次数
            watch_num = 1
            while(True):
                sleep(8 +random.randint(0,8))
                swipeUp(1000,-0.1)

                # 根据时间判断 两个小时结束
                cur = datetime.datetime.now()
                timeStyle=cur.strftime("%Y-%m-%d %H:%M:%S")
                strlog = '查看一个东方头条小视频，已看%d个' % watch_num
                strlog =strlog +timeStyle+'\n'
                f.write(strlog)
                print(strlog)
                watch_num += 1
                if((cur-start).seconds >= 3600*2):
                    break
        else:
            f.write("左上角ImageView不存在" + '\n')
    else:
        f.write("上方小视频按钮不存在" + '\n')
else:
    f.write("主页视频按钮不存在" + '\n')
f.close()

stop_app("com.songheng.eastnews")
