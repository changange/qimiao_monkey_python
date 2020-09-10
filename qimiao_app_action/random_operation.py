import qimiao_app_comm.app_start as start
import xml.etree.ElementTree as ET
import random
import math
import os, datetime
import time
import qimiao_app_comm.qimiao_comm as comm

class RandomAction:

    def __init__(self, cmd_name):
        self.cmd_name = cmd_name
        self.d = start.TestStart().connCMD(cmd_name)
        self.s = start.TestStart().sessionConn(cmd_name)
        self.display = self.d.device_info["display"]
        self.width = self.display['width']
        self.height = self.display['height']

        self.clickRetrn = comm.DoubleClick()
        print(f'{self.width}--{self.height}')

    #   随意点击、滑动
    def radom_click_liding(self):
        resT = self.read_config(f'{os.path.abspath("..")}\config\monkey.xml')
        resTD = float(resT[0]) * 100
        resS = float(resT[1]) * 100
        resB = float(resT[2]) * 100

        num = random.randint(0, 100)
        # print(f'产生的随机数是：{num}')

        if 0 <= num and num < resTD:
            #   点击
            W = random.randint(0, self.width)
            H = random.randint(math.trunc(0.0468*self.height), self.height)

            if H > 0.85*self.height and W>0.47*self.width and H<0.884*self.height and W<0.583*self.width:
                print('点到了不该点的地方~~~~~~')
                return False;
            self.d.click(W, H)
            #print(f'点击位置：{W}<-->{H}')
            print('点击-->操作执行完成')

            #   不可以连续两次点击返回键
            self.clickRetrn.set_count(1)

            #   到时间点击确定
            # print(f'当前是秒：{datetime.datetime.now().second}')
            if datetime.datetime.now().second%30 == 0:
                print('30秒已到，点击确定~~~')
                self.d.click(self.width * 0.686, self.height * 0.61)
                print('确定 点击完成了~~~~~~~~')

            if datetime.datetime.now().second % 5== 0:
                print('5秒时间已到，点击取消~~~')
                self.d.click(self.width * 0.299, self.height * 0.61)
                print(f'取消 点击完成了~~~~~~~~{self.width * 0.29}<-->{self.height * 0.61}')

            #   优化项 有些手机上有虚拟home键，点到这个键后重新启动APP
            if H >= math.trunc(self.height*0.947) and math.trunc(self.width*0.2) <= W and W <= math.trunc(self.width*0.8):
                print('点击到了危险区域，将要重启APP~~~')
                print(f'{H}->{math.trunc(self.height*0.947)}  {W}-->{math.trunc(self.width*0.2)}=={math.trunc(self.width*0.8)}')

                ##  启动APP
                print("------------------开始再次点击APP")
                try:
                    self.s.press('home')
                    time.sleep(0.2)
                    self.s.press('home')
                    time.sleep(0.3)
                    self.d.swipe(self.width * 0.9, self.height * 0.64, self.width * 0.15, self.height * 0.65)
                    time.sleep(0.2)
                    self.d.swipe(self.width * 0.9, self.height * 0.64, self.width * 0.15, self.height * 0.65)
                    self.s(text='奇妙派对').click()
                    time.sleep(0.5)
                except Exception as e:
                    print("~~~~~~~~~~~~~~~再次点击APP异常")
                    print(e)

                ##  self.d.app_start('com.qmnl.qmpd', activity='com.qmnl.pati.ui.SplashActivity')

        if resTD <= num and num < resS + resTD and resTD != (resS + resTD):
            #   滑动
            w_stat = random.randint(0, self.width)
            h_stat = random.randint(math.trunc(0.0468*self.height), self.height)
            w_end = random.randint(0, self.width)
            h_end = random.randint(0, self.height)
            #print(f'滑动的设备：{self.cmd_name}')
            print(f'当前滑动的坐标：{w_stat}<->{h_stat}：{w_end}<-->{h_end}')
            try:
                self.d.swipe(w_stat, h_stat, w_end, h_end)
            except Exception as e:
                print('滑动可能报错了~~~')
                print(e)
            # print(f'滑动位置{w_stat}：{h_stat}<--->{w_end}：{h_end}')
            print('滑动-->操作执行完成')

            #   不可以连续两次点击返回键
            self.clickRetrn.set_count(1)

        if resS + resTD <= num and num < resB + resS + resTD and resS + resTD != resB + resS + resTD:
            #   返回
            if self.clickRetrn.get_count() == 1:
                self.d.press('back')
                print('返回-->操作执行完成')

                #   不可以连续两次点击返回键
                self.clickRetrn.set_count(0)
            else:
                print('不可以连续两次点击返回键~~~')

    def read_config(self, path):
        res=[]
        tree = ET.parse(path).getroot()
        i =  tree.find('Doaction')
        click = i.find('click').text
        res.append(click)
        back = i.find('back').text
        res.append(back)
        sliding = i.find('sliding').text
        res.append(sliding)
        return res

if __name__ == '__main__':
    # r = RandomAction('UKPFSCEQ99999999')
    r = RandomAction('LFLBB19418208291')
    while True:
        r.radom_click_liding()