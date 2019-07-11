# coding=utf-8
"""
queue中，put和get的参数里默认拥有一个block参数，默认为True，即为在插入队列为满或者取出为空时
默认为阻塞状态，等待取出取出或者插入数据。
"""

from queue import Queue
import time
import threading


def put_value(q):
    index = 0
    # another = 1
    while True:
        q.put(index)
        # q.put(another)
        index += 1
        # another += 1
        time.sleep(2)


def another_put_value(q):
    another = 2
    while True:
        q.put(another)
        another += 2
        time.sleep(1)


def get_value(q):
    while True:
        print(q.get())


def main():
    q = Queue(5)
    p = threading.Thread(target=get_value, args=(q, ))
    a_p = threading.Thread(target=another_put_value, args=(q, ))
    g = threading.Thread(target=put_value, args=(q, ))

    p.start()
    a_p.start()
    g.start()


if __name__ == '__main__':
    main()