import qimiao_app_comm.app_start as start
import  concurrent.futures
import datetime
import os, re, time

class ActionLog:
    def __init__(self):
        self.phone_number = start.TestStart().connectMoblie()
        self.log_path = "E:\qimiao_log"

    # 创建文件（有几个adb devices就创建几个）
    def create_log_text(self, p_num):
        print("创建文件")
        now = str(datetime.datetime.today().date())
        path = self.log_path + "\\" + now + "_" + p_num + ".txt"
        if os.path.exists(path):
            # print("日志文件已存在")
            return path
        try:
            open(path, 'a');
            return path
        except Exception as e:
            print(e)
            return ""

    #执行CMD
    def execute_cmd(self,p_num):
        cmd_string = f"adb -s {p_num} shell dumpsys meminfo com.qmnl.qmpd"
        res_string = os.popen(cmd_string).readlines()
        # 拿到有用行的数据
        # old = [res_string[5],res_string[7],res_string[8]]
        old = [res_string[7],res_string[8]]

        res_list=[]

        for i in old:
            res_cmd = i.replace(" ", "|")
            patern = re.compile(r'\d+')
            list = patern.findall(res_cmd)
            res_list.append(list[-3])
            res_list.append(list[-2])
            res_list.append(list[-1])
        print(res_list)
        return res_list

    #字符串拼接
    def join_str(self,cmd_list):
        now_time = str(datetime.datetime.now()) + "\n"
        res_head = "\t\t\t\tHeap\tHeap\tHeap\n" + "\t\t\t\tSize\tAlloc\tFree\n"
        res_boby = "\t\t\t\t------\t------\t------\n"
        res_foat_one = f"Native Heap\t\t{cmd_list[0]}\t{cmd_list[1]}\t{cmd_list[2]}\n"
        res_foat_two = f"Dalvik Heap\t\t{cmd_list[3]}\t{cmd_list[4]}\t{cmd_list[5]}\n"
        res_str = "\n================================================================\n\n"
        res_end =now_time + res_head + res_boby + res_foat_one + res_foat_two + res_str
        # print(res_end)
        return res_end

    #写入log
    def write_log(self, path,text):
        with open(path, "a") as f:
            f.write(text)
        print("写入完成")

    # main函数
    def test_mian(self, p_num):
        #创建
        log_path = self.create_log_text(p_num)
        #执行
        res_list = self.execute_cmd(p_num)
        #拼接
        res_str = self.join_str(res_list)
        #写入文件
        self.write_log(log_path, res_str)


    def qimiao_threading_excution(self):
        if len(self.phone_number) >=1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.phone_number)) as excutor:
                for i in range(len(self.phone_number)):
                    excutor.submit(self.test_mian, self.phone_number[i])

        else:
            print('adb无法连接到手机~~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == '__main__':
    a = ActionLog();
    while(True):
        a.qimiao_threading_excution()
        time.sleep(10)
    # a.join_str(['535552', '498042', '37509', '23205', '11603', '11602'])
    # print(datetime.datetime.today().date())