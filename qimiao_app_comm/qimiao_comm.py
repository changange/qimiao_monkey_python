import qimiao_app_comm.app_start as start
import datetime

class QimiaoCommnotAction:

    ##  滑动的起始位置和终止位置（百分比）
    def side(self,start_width, start_hight, end_width, end_hight, cmd_name):
        s = start.TestStart().sessionConn(cmd_name)
        s.swipe(start_width, start_hight, end_width, end_hight)

    def cc(self):
        time = datetime.datetime.now().second
        print(time.second)

if __name__ == '__main__':
    q = QimiaoCommnotAction()
    q.cc()