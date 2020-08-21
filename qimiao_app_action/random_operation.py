import qimiao_app_comm.app_start as start
import xml.etree.ElementTree as ET
import random
import math
import os, datetime

class RandomAction:

    def __init__(self, cmd_name):
        self.cmd_name = cmd_name
        self.d = start.TestStart().connCMD(cmd_name)
        self.display = self.d.device_info["display"]
        self.width = self.display['width']
        self.height = self.display['height']
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
            self.d.click(W, H)
            print(f'点击位置：{W}<-->{H}')
            print('点击-->操作执行完成')

            #   到时间点击确定
            print(f'当前是秒：{datetime.datetime.now().second}')
            if datetime.datetime.now().second%15 == 0:
                print('30秒已到，点击确定~~~')
                self.d.click(self.width * 0.686, self.height * 0.61)
                print('确定 点击完成了~~~~~~~~')

            if datetime.datetime.now().second % 20== 0:
                print('20秒时间已到，点击取消~~~')
                self.d.click(self.width * 0.299, self.height * 0.61)
                print(f'取消 点击完成了~~~~~~~~{self.width * 0.29}<-->{self.height * 0.61}')

            #   优化项 有些手机上有虚拟home键，点到这个键后重新启动APP
            if H >= math.trunc(self.height*0.947) and math.trunc(self.width*0.2) <= W and W <= math.trunc(self.width*0.8):
                print('点击到了危险区域，将要重启APP~~~')
                print(f'{H}->{math.trunc(self.height*0.947)}  {W}-->{math.trunc(self.width*0.2)}=={math.trunc(self.width*0.8)}')
                ##  启动APP
                self.d.app_start('com.qmnl.qmpd', activity='com.qmnl.pati.ui.SplashActivity')

        if resTD <= num and num < resS + resTD and resTD != (resS + resTD):
            #   滑动
            w_stat = random.randint(0, self.width)
            h_stat = random.randint(math.trunc(0.0468*self.height), self.height)
            w_end = random.randint(0, self.width)
            h_end = random.randint(0, self.height)
            print(f'滑动的设备：{self.cmd_name}')
            print(f'当前滑动的坐标：{w_stat}<->{h_stat}：{w_end}<-->{h_end}')
            try:
                self.d.swipe(w_stat, h_stat, w_end, h_end)
            except Exception as e:
                print('滑动可能报错了~~~')
                print(e)
            # print(f'滑动位置{w_stat}：{h_stat}<--->{w_end}：{h_end}')
            print('滑动-->操作执行完成')

        if resS + resTD <= num and num < resB + resS + resTD and resS + resTD != resB + resS + resTD:
            #   返回
            self.d.press('back')
            print('返回-->操作执行完成')

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