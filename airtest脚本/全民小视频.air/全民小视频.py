# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)


devs = device()
# print(devs.list_app(third_only=True))

# 先关闭视频app
stop_app("com.baidu.minivideo")

# 启动app 等待5秒
start_app("com.baidu.minivideo",activity=None)

sleep(5.0)
# 1、青少年模式 跳过
obj =poco(text='我知道了',type='android.widget.RadioButton')
if obj.exists():
    obj.click()

# 2、每日签到
mybtn=poco("android.widget.LinearLayout").offspring("com.baidu.minivideo:id/root_view").offspring("com.baidu.minivideo:id/tab_4_icon")
if mybtn.exists():
    mybtn.click()                 
taskbtn=poco("android.widget.LinearLayout").offspring("com.baidu.minivideo:id/container").offspring("com.baidu.minivideo:id/activity_banner_container").offspring("android.widget.FrameLayout").offspring("com.baidu.minivideo:id/sdv_my_live")
        
if taskbtn.exists():
    taskbtn.click()
sleep(15.0)    


#自定义滑动事件
def getSize():
    s=poco.get_screen_size()
    return (s[0], s[1])
#屏幕向上滑动
def swipeUp(t,percent):
    l = getSize()
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 1.0)   #起始y坐标
    y2 = int(l[1] * percent)   #终点y坐标
    swipe((x1, y1), (x1, y2),t)
#屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    swipe((x1, y1), (x1, y2),t)
#屏幕向左滑动
def swipLeft(t):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    swipe((x1,y1),(x2,y1),t)
#屏幕向右滑动
def swipRight(t):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    swipe((x1,y1),(x2,y1),t)    

    
swipeUp(1000,0.1)    
# 3、日常任务 观看视频
seemovie =poco(text ='签到后看视频，每20秒可得2钻石，奖励记录将在第二天展示在钻石列表里哦',type='android.view.View')
if seemovie.exists():
    seemovie.click()

# 开始观看视频
poco(name='com.baidu.minivideo:id/index_img_play',type='android.widget.ImageView').click()

# 查看次数
watch_num = 1
# 分享次数
share_num = 1

while True:
    #等待18秒
    sleep(18)
    swipeUp(1000,0.3)
    print('查看一个视频，已看%d个' % watch_num)
    
    print('分享视频：%d' % share_num)
    #分享次数
    if share_num <= 5:        
        share_btn = poco(name='com.baidu.minivideo:id/detail_bottom_share_icon',type='android.widget.ImageView') 
        if(share_btn.exists()):
            share_btn.click()
            # 注意：可能调用不起来分享对话框
            share_weixin =poco('com.baidu.minivideo:id/share_weixin')
            while not share_weixin.exists():
                share_btn.click()
            
            share_weixin.click()
            sleep(5)
            # 选择好友
            group=poco(name='com.tencent.mm:id/rd',text='王攀峰')
            
            if(group.exists()):
                group.click()  
                sleep(5)
                shareFinal=poco(name='com.tencent.mm:id/b29',text='分享')
                if(shareFinal.exists()):
                    shareFinal.click()
                    sleep(5)
                    backbtn =poco(name='com.tencent.mm:id/b28',text='返回全民小视频')
                    if(backbtn.exists()):
                        backbtn.click()
                        share_num += 1
                        sleep(5)
        
    sleep(18)
    watch_num += 1
    if(watch_num>=20):
        break
        