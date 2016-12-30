from math import pi
from string import Template
import string
a1 = 'Pi with three decimals: %.3f'
print(a1 % pi)

a2 = Template('$x, glorious $x!')
print(a2.substitute(x='ZYQ'))#substitute方法返回值为字符串

s = Template('A $thing must never $action')
d = {}#通过字典给模板的多个变量赋值
d['thing'] = 'gentleman'
d['action']= 'show his socks'
t = {}
t['thing'] = 'gentleman'
print(s.substitute(d))
print(s.safe_substitute(t))#使用带有safe的语句可以有缺省的变量值！！！

seq = ['1','2','3','4','5']
sep = '+'
print(sep.join(seq))
dirs = '','usr','bin','env'
print('/'.join(dirs))
print(sep.join(seq).split('+'))

str1 = 'ZYQ'
print(str1.lower())
#我们能够利用lower将数据形式转换成相同情况。
name = "ZYQ"
names = ['HJT','FCK','HSZ','ZYQ']
for nam in names:
    print(nam.lower().title())#title()\lower()相对应的方法
    print(string.capwords(nam))#利用string模块的capwords函数

print('ZYQ'.islower())
print('ZYQ'.isupper())
print('Zyq'.islower())
print('zYq'.islower())
#replace 中所有匹配项均可匹配
print('That is very easy!'.replace('That','This'))

table = str.maketrans('cs','kz')
print(len(table))
print('This is an incredible test'.translate(table))



