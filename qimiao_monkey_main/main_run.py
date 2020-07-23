import qimiao_app_comm.app_start as start
import  concurrent.futures
import qimiao_app_action.random_operation as action
import multiprocessing
import time, os


class MainTest:

    def test_main(self, cmd_name):
        ##APP日志操作   清空
        start.TestStart().clear_cache_log(cmd_name)
        start.TestStart().delete_mobile_log(cmd_name, 'qimiao_log')     ##  文件夹

        monkey = action.RandomAction(cmd_name)

        ##  启动APP
        start.TestStart().openQimiao(cmd_name)

        print('开始执行monkey测试')
        while True:
            monkey.radom_click_liding()


    def qimiao_threading_excution(self):
        phone_number = start.TestStart().connectMoblie()

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as excutor:
            if len(phone_number) >= 1:
                for i in range(len(phone_number)):
                    excutor.submit(self.test_main, phone_number[i])
                    # time.sleep(3)
                    # excutor.submit(start.TestStart().save_app_log, phone_number[i], 'qimiao_log')
            else:
                print('adb无法连接到手机~~~')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



        # processes = []
        # for i in range(len(phone_number)):
        #     phone_number[i] = multiprocessing.Process(target=self.test_main(phone_number[i],))
        #     processes.append(phone_number[i])
        #     processes.append(multiprocessing.Process(target=start.TestStart().save_app_log(phone_number[i], 'qimiao_log')))
        #
        #     for p in processes:
        #         p.start()
        #
        #     for p in processes:
        #         p.join()


if __name__ == '__main__':
    mainT = MainTest()
    mainT.qimiao_threading_excution()