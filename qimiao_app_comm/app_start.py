import uiautomator2 as u2
import os
import time

class TestStart:

    def connCMD(self, cmd_name):
        # return u2.connect_usb()
        # return u2.connect_wifi('172.16.1.32')
        return u2.connect(cmd_name)

    def sessionConn(self, cmd_name):
        return self.connCMD(cmd_name).session(package_name='com.qmnl.qmpd', attach=True)


    @staticmethod
    def connectMoblie():
        res_adb = []
        res_connnect = os.popen('adb devices')
        output_str = res_connnect.readlines()
        for i in range(len(output_str)):
            if '\tdevice' in output_str[i]:
                num = output_str[i].find('\t')
                del_str = output_str[i][0: num]
                res_adb.append(del_str)
        return res_adb


    def openQimiao(self,cmd_name):
        d = self.connCMD(cmd_name)

        d.app_start('com.qmnl.qmpd', activity='com.qmnl.pati.ui.SplashActivity')
        # s = self.sessionConn(cmd_name)
        # time.sleep(2)

        # for i in range(5):
        #     if s(resourceId='com.qmnl.qmpd:id/home_fragment_surprise_box_image'):
        #         print ('APP 启动成功')
        #         return True
        #     else:
        #         time.sleep(3)
        # print ('APP 启动失败')
        # return False

    ##  清空日志缓存
    def clear_cache_log(self, phone_num):
        cmd_clear = f'adb -s {phone_num} logcat -c'
        print(cmd_clear)
        os.popen(cmd_clear)
        print('日志缓存清空完成')


    ##  手机端日志删除等操作
    def delete_mobile_log(self, cmd_name, log_file):
        cmd_ls = f'adb -s {cmd_name} shell ls /data/local/tmp/'
        res_ls_old = os.popen(cmd_ls).readlines()
        res_ls_new = map(lambda x:x.strip(), res_ls_old)

        ##  如果有日志文件夹就清空
        if log_file in res_ls_new:
            print('日志文件夹已存在,删除~~~')
            cmd_dele = f'adb -s {cmd_name} shell rm -rf /data/local/tmp/{log_file}'
            print(cmd_dele)
            os.popen(cmd_dele)

        time.sleep(1)
        print('=====================================================')
        cmd_creat = f'adb -s {cmd_name} shell mkdir /data/local/tmp/{log_file}'
        print(cmd_creat)
        res_creat = os.popen(cmd_creat)
        if len(res_creat.readlines()) == 0 :
            print('APP日志文件创建成功')
        else:
            print('APP日志文件创建失败')

    ##  监听日志
    def save_app_log(self, cmd_name, log_file):
        print('启动监听日志')
        cmd_save_log = f'adb -s {cmd_name} logcat -v threadtime -f /data/local/tmp/{log_file}/log_{cmd_name} -n 10 -r 2000 -s Unity *:E'
        # cmd_save_log = f'adb -s {cmd_name} logcat -v threadtime -f /data/local/tmp/{log_file}/log_{cmd_name} -n 10 -r 2000 *:I'
        print(f'----{cmd_save_log}')
        cc = os.popen(cmd_save_log)
        # for i in len(cc.readlines()):
        #     print(i)



if __name__ == '__main__':
    t = TestStart()
    t.sessionConn('UKPFSCEQ99999999').click()
