
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random
import time
import datetime
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

def randomSwipeUp():
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
    
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

devs = device()
print(devs.list_app(third_only=True))

userList=[]
def loadUser():
    f = open("D:\kuaishou.txt") 
    for line in f:
        print(line)
        userList.append(line)
    f.close()
#登录 直接从领取红包界面进入
def login(index):
    getAward = poco(name="com.kuaishou.nebula:id/negative",text="立即领取")
    getAward.click()
    sleep(5)
    
    phone= poco(name ="com.kuaishou.nebula:id/phone_login_text",text="手机号登录")
    phone.click()
    sleep(5)
    
    x=userList[index].split('----')
    text(x[0])
    sleep(5)
    
    nextstep =poco(name="com.kuaishou.nebula:id/next_view",text="下一步")
    nextstep.click()
    sleep(5)
    
    mima =poco(name="com.kuaishou.nebula:id/forget_psd_btn",text="收不到验证码，使用快手密码登录")
    mima.click()
    sleep(5)

    text(x[1].strip())
    sleep(5)
    
    log =poco(name="com.kuaishou.nebula:id/login_view",text="登录")
    log.click()
    sleep(25)
    
    #可能有弹窗 关闭青少年弹窗
    swipeUp(1000,0.5)
    
    
# 清理APP数据
def clearAPP():
    home()
    setting =poco(name='设置',type='android.widget.TextView')
    if(setting.exists()):
        setting.click()
        sleep(3)
        swipeUp(1000,0.4)
        sleep(3)
        app = poco(name ='com.android.settings:id/title',text='应用')
        if(app.exists()):
            app.click()
            sleep(3)
            
            ks =poco(name ="com.android.settings:id/app_name",text="快手极速版")
            if(ks.exists()):
                ks.click()
                sleep(3)
                
                cl=poco(name="com.android.settings:id/right_button",text="清除数据")
                cl.click()
                sleep(3)
                confirm =poco(name="android:id/button1",text="确定")
                if(confirm.exists()):
                    confirm.click()
                    sleep(3)
    home()            
    return 0


# ================================================
# 快手极速版
# 先关闭视频app
file = r'D:\快手极速版.log'
f = open(file, 'a+')
loadUser()

index=0
# 14个账号
while(index<14):
    stop_app("com.kuaishou.nebula")
    clearAPP()
    start_app("com.kuaishou.nebula",activity=None)
    # 等待80秒启动加载
    sleep(80)
    login(index)
    watch_num=0
    #开始看视频
    start = datetime.datetime.now()
    while(True):
        sleep(8 +random.randint(0,8))
        randomSwipeUp()        
        # 根据时间判断 三个小时结束
        cur = datetime.datetime.now()
        timeStyle=cur.strftime("%Y-%m-%d %H:%M:%S")
        strlog = '查看一个快手极速视频，已看%d个' % watch_num
        strlog =strlog +timeStyle+'\n'
        f.write(strlog)
        print(strlog)
        watch_num += 1
        f.flush()
        if((cur-start).seconds >= 3600*3):
            break
f.close()

# 关闭视频app
stop_app("com.kuaishou.nebula")        
        

        



