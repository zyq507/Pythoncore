a = 'Hello'
b = 'World'

print(a+b)
print(a,b)#使用逗号输出时两个变量之间会有空格

t = [1,2,3,4]
a,b,*rest = t#可以使用该语句来获取剩余的变量
print(a,b,rest)

#链式赋值，从左到右赋值
x = y = [1,2,2]
print(x,y)
word1 = 'foo'
word2 = 'bar'
word1 += word2
print(word1)#增量表达式可以用在字符串的赋值上
'''
name = input('What\'s your name ?\n')
if name == 'ZYQ':
    print('Hello! ZYQ')
else:
    print('Hi! stranger~')
'''
'''
nn = input('get a word \n') or 'unkown'
print(nn)#此时如果不输入名字的话，直接赋值给nn字符串‘unknown’
'''
'''
name = ''
while not name.strip(' s'):#使用strip()方法可以除去字符串两侧的空格
    name = input('Hi')#此时S和空格也被除去了
print(name)
'''
'''
#并行迭代
names = ['A','B','C','D']
ages = [1,4,2,3]
for name,age in zip(names,ages):
    print(name,'is',repr(age),'old')
'''

#列表推导式
print([x*x for x in range(4)])#0 1 2 3的平方
print([x*x for x in range(10) if x % 3 == 0])#条件语句加上循环语句生成

exec("print('Hello, World!')")
stys = ['a','b','v','d','ss']
for a,b  in enumerate(stys):
    print(a,b)
#输出索引值对，enumerate反馈回迭代器





