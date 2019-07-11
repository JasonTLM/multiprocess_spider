# coding=utf-8
# import math
# import numpy
#  = 'abc123def'
# patt1 = /[0-9]+/
from queue import Queue
import time
import threading


def put_value(q):
    index = 0
    # another = 1
    while index <= 5:
        q.put(index)
        # q.put(another)
        index += 1
        # another += 1
        time.sleep(2)

def test_q(q):
    print(q)

# def another_put_value(q):
#     another = 2
#     while True:
#         q.put(another)
#         another += 2
#         time.sleep(1)
#
#
# def get_value(q):
#     while True:
#         print(q.get())


def main():
    q = Queue(5)
    p = threading.Thread(target=put_value, args=(q, ))
    t = threading.Thread(target=test_q, args=(q,))
    p.start()
    t.start()

    # p = threading.Thread(target=get_value, args=(q, ))
    # a_p = threading.Thread(target=another_put_value, args=(q, ))
    # g = threading.Thread(target=put_value, args=(q, ))
    #
    # p.start()
    # a_p.start()
    # g.start()


if __name__ == '__main__':
    main()
