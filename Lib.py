import sys
import os#操作系统的服务功能
import copy
import webbrowser
sys.path.append('G:/Pythoncore')#该函数可以用来添加路径。
import LibTest

LibTest.Hello()

dir(copy)
print(copy.__all__)
help(copy.copy)
#print(copy.__doc__)
print(copy.__file__)#包所在的位置


print(sys.platform)#输出程序执行的平台
print(os.sep.join(['192','168','253','1']))
#os.sep代表了用于路径名中的分隔符
print(os.sep)
print(os.linesep)#\r\n

#webbrowser.open('http://www.python.org')#可以用来打开网页
#os.system(r'G:\ZEAL_SVN\Balance_Car\Doc\hello.txt')
#可以用来打开文件

import time

print(time.asctime())#显示当前时间
print(time.time())#直接输出秒数
print(time.localtime())
import random





