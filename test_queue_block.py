# coding=utf-8
import threading
import time
from queue import Queue


def test1(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(0.5)


def test2(q):
    pass


def test3(q):
    pass


def get_value(q):
    while True:
        print(q.get())


def main():
    q = Queue(4)
    t1 = threading.Thread(target=test1, args=(q, ))
    t2 = threading.Thread(target=test2, args=(q, ))
    t3 = threading.Thread(target=test3, args=(q, ))

    t1.start()
    t2.start()
    t3.start()

    g = threading.Thread(target=get_value, args=(q, ))
    g.start()




if __name__ == '__main__':
    main()