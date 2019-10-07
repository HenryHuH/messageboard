# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import datetime
import random
from airtest.core.api import *
from airtest.core.android.minitouch import *
from poco.utils.track import MotionTrack

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
    y1 = int(l[1] * 0.8)  #起始y坐标
    y2 = int(l[1] * percent)   #终点y坐标

    swipe((x1, y1), (x1, y2),t+random.randint(0,20))
    
def test():
    #全部随机 随机减
    x1 = 0.4-random.uniform(0,0.2)
    y1 = 0.7-random.uniform(0,0.1)

    #随机加 
    x2 = 0.1 + random.uniform(0,0.1)
    y2 = -0.1 + random.uniform(0,0.2)
    
    #生成十个中间点
    xn=[]
    yn=[]
    i=0
    while(i<20):
        xn.append(random.uniform(x1,x2))
        yn.append(random.uniform(y1,y2))
        i =i+1
    xn.sort(reverse = True)    
    yn.sort(reverse = True)

    tracks = [MotionTrack().start([x1, y1]).move([xn[0], yn[0]]).move([xn[1], yn[1]]).move([xn[2], yn[2]]).move([xn[3], yn[3]]).move([xn[4], yn[4]]).move([xn[5], yn[5]]).move([xn[6], yn[6]]).move([xn[7], yn[7]]).move([xn[8], yn[8]]).move([xn[9], yn[9]]).move([xn[10], yn[10]]).move([xn[11], yn[11]]).move([xn[12], yn[12]]).move([xn[13], yn[13]]).move([xn[14], yn[14]]).move([xn[15], yn[15]]).move([xn[16], yn[16]]).move([xn[17], yn[17]]).move([xn[18], yn[18]]).move([xn[19], yn[19]]),]       
    poco.apply_motion_tracks(tracks)
    sleep(8)
    
while(True):
    test()
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