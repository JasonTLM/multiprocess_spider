# coding=utf-8
import copy
from PIL import Image

a = [1,2,3,[4,5,6,7,0],8,9,10]
# a.append(11)
b = a.copy()
c = copy.deepcopy(a)
b.append(11)
a.append(12)
a[3].append(100)
print("a:",a)
print("--"*20)
print("b:",b)
print("--"*20)
print("c:",c)
