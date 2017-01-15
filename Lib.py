import sys
import copy
sys.path.append('G:/Pythoncore')#该函数可以用来添加路径。
import LibTest

LibTest.Hello()

dir(copy)
print(copy.__all__)
help(copy.copy)
#print(copy.__doc__)
print(copy.__file__)#包所在的位置
