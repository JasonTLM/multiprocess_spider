# coding=utf-8

import threading
import time
import random

gMoney = 1000
gCondition = threading.Condition()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            p_money = random.randint(300,1000)
            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                break
            gMoney += p_money
            print("%s号生产了%d元钱， 此时总共%d元钱" %
                  (threading.current_thread().name, p_money, gMoney))
            gTimes += 1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            c_money = random.randint(500,1500)
            gCondition.acquire()
            while gMoney < c_money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print("%s号需要消费%d元钱， 此时总剩余%d元钱， 故不足于满足此时消费！" %
                      (threading.current_thread().name, c_money, gMoney))
                gCondition.wait()
            gMoney -= c_money
            print("%s号需要消费%d元钱， 消费后剩余%d元钱" %
                  (threading.current_thread().name, c_money, gMoney))
            gCondition.release()
            time.sleep(0.5)


def main():
    for i in range(3):
        c = Consumer(name="消费者线程%d" % i)
        c.start()

    for x in range(4):
        p = Producer(name="生产者线程%d" % x)
        p.start()


if __name__ == '__main__':
    main()