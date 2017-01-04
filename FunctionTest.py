#函数的参数处理很是重要
#文档化函数
def fibs(num):
    'This is a fib function~'#函数注释
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print(fibs(3))
print(fibs.__doc__)#前后均为双下划线

#函数不会改变外部的赋值
#函数可以对可变数据结构进行改变

def nameinit(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.spilt()
    if len(names) == 2:names.insert(1,'')
    labels = 'first','middle','last'
    for label, name in zip(labels, names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]#保证存储的是数组
            
#如果要求原地修改，那么就使用列表方式：
def inc1(num):
    return num + 1

def inc2(num): num[0] = num[0] + 1

tt = [10]
print(inc1(10))#有返回值自加1
print(inc2(tt))#此时没有返回值
print(tt)#修改了列表
#位置参数 与 关键字参数
def printTest(a,b,c=2, *poss,**keys):#**收集关键字参数，*收集位置参数
    print(a,b,c)
    print(poss)
    print(keys)

printTest(1,2,3,4,5,foo=1,pp =2) 

def Story(**paras):
    print('My name is %(name)s, I\'m %(age)s old.' %paras)
    #   %()s 这种写法一定要搞清楚

Story(name = 'ZYQ',age = '21')#关键字参数一定记得写上关键字

def ppp(x,y,*other):#*other将会返回一个元组
    print('This is'+str(other))
    return x + y

ppp(1,2,'Hello World!','ZYQ')#其他参数将会返回到元组之中

def Interval(start,stop = None,step = 1):
    'Imitate range() for step >0'
    if stop is None:#is是同一性运算符
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(Interval(5))
print(Interval(2,10))
print(Interval(2,8,2))
print(Interval(3,8))
print(ppp(*Interval(3,7)))#必须使用*使变量作为剩余参数。
        
#递归方法
#1、阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)#递归调用的方法

print(factorial(5))
#二分法查找(序列已经排序完成)
def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[lower]#保证所查找的数字一定会被找到
        return lower
    else:
        middle = (lower + upper)//2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [34 ,67,8,123,4,100,95]
seq.sort()
#bisect模块非常好用
print(search(seq,34))
print(search(seq,100))
import bisect
print(bisect.bisect(seq,34))
#map函数返回函数作用下的值str作用下的range(10)
print(list(map(str,range(10))))
