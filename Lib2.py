import random
import shelve
a = [1,2,3,4,5,6]
b = random.shuffle(a)#将给定的列表随机移位，不返回新的列表b = None
print(b)
print(a)
#shelve模块，微型数据库
s = shelve.open('test.dat')
s['x'] = ['a','b','c']
temp = s['x']#先取出暂时量
temp.append('d')
s['x'] = temp#之后再存回数据库
print(s['x'])

