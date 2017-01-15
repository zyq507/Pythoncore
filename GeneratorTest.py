__metaclass__ = type

a = [[2,4],[3,[4,5],4],4,[4,4]]
#判断输入的元素是否为字符串（元素！）
def isstr(val):
    try:
        val + ''           #判断能否与''加和
    except TypeError: pass #说明输入变量不是字符串
    else: raise TypeError  #说明输入变量为字符串
    
#递归的：1、基本情况  2、需要递归的情况
def Go(ls):
    try:
        isstr(ls)
        for sub in ls:       #首先展开ls列表
            for x in Go(sub):#对ls列表的每一项进行Go()访问
                yield x      #输出Go()中获得的常量
    except TypeError:        #如果从某一项不能Go()访问，说明为列表中的常量
        yield ls             #直接输出常量

print(list(Go(a)))#输出所有值


#生成器方法：send方法
def repeater(value):
    while True:
        new = (yield value)
        if new is not None: new = value








    
