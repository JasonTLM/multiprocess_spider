# coding=utf-8

import threading
import random
import time


gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            p_money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += p_money
            print("%s生产了%d元钱， 剩余%d元钱" %
                  (threading.current_thread().name, p_money, gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            c_money = random.randint(300,1500)
            gLock.acquire()
            if gMoney >= c_money:
                gMoney -= c_money
                print("%s消费了%d元钱， 剩余%d元钱" %
                      (threading.current_thread().name, c_money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print("%s准备消费%d元钱， 实际只有%d元钱， 故不足以支撑该次消费！" %
                      (threading.current_thread().name, c_money, gMoney))
            gLock.release()
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