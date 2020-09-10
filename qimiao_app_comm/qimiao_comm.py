import qimiao_app_comm.app_start as start
import datetime
import time

class QimiaoCommnotAction:

    ##  滑动的起始位置和终止位置（百分比）
    def side(self,start_width, start_hight, end_width, end_hight, cmd_name):
        s = start.TestStart().sessionConn(cmd_name)
        s.swipe(start_width, start_hight, end_width, end_hight)

    def cc(self):
        time = datetime.datetime.now().second
        print(time.second)

    ##  截图
    def jieTu(self, cmd_name):
        s = start.TestStart().sessionConn(cmd_name)
        screen_name = time.strftime('%Y%m%d_%H%M%S.png')
        s.screenshot(filename='E:/log/tu/' + screen_name)

##  返回事件不能连续两次
class DoubleClick:
    __count = 0;

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls,num):
        cls.__count = num

if __name__ == '__main__':
    # q = QimiaoCommnotAction()
    # q.cc()

    # f2 = DoubleClick()
    # DoubleClick.set_count(10)
    # print(f2.get_count())
    # f1 = DoubleClick()
    # print(f1.get_count())

    q =QimiaoCommnotAction()
    q.jieTu('UKPFSCEQ99999999')
