#列表方法试验
a = [1,2,3]
a.append(4)
print(a)

t = [1,2,3,3,4,5,6,8,8,9]
print(t.count(3))
print(t.count(8))

en1 = [1,3,4]
en2 = [2,2,4]
print(en1+en2)                  #加法链接不会改变原有的en1与en2
print(en1,en2)
print(en1.extend(en2))          #返回值为None
print (en1)                     #extend方法会改变原列表

#或者使用以下方法
en1 = [1,3,4]
en2 = [2,2,4]

en1[len(en1):]=en2
print(en1)

t = [1,2,3,3,4,5,6,8,8,9]
print(t.index(8))#只返回第一个找到的元素，并非所有

aa = ['Who', 'are', 'you', '?']
print(aa.index('are'))#列表的索引从0开始

num = range(7)
print(num)#range返回的不是一个列表，返回的应该是一个迭代器
print(list(num))

nums = [1,2,3,4,5,6,7]
nums.insert(4,0)
nums.insert(5,'HaHa')#列表储存的类型不一定是同一种
nums.insert(3,['a','b','c'])

print(nums[3:5].insert(1,2))
print(nums)


xx = [1,2,3,4]
xx.pop(1)
print(xx)
xx.pop()
print(xx)#pop可以随意出栈列表里的任意一个元素

bb = [1,1,33,24,53]
bb.remove(1)
print(bb)
#remove只会移除列表里面匹配的第一项，而且它没有返回值，会改变原来的列表。
cc = [1,2,3]
cc.reverse()
print(cc)
#存在reversed方法，返回迭代器，可以用list函数打开
for i in reversed(range(4)):
    print(repr(i)+'\t')
#reversed返回迭代器(iterator)，可以用list()函数解开

#sort方法，重要！！！
#原位置排序
xxa = [4,6,2,1,7,9]
yy = xxa[:]#相当于把xxa完全复制给了yy
yy.sort()
#print('Python'.sort())是错误的
print(yy)
#sorted可用于任何列表
print(sorted('Python'))

#高级排序
nums = ['ss','sssa','sa','eessfd']
nums.sort(key = len)
print(nums)
nums = ['ss','sssa','sa','eessfd']
nums.sort(key = len,reverse = True)
print(nums)

#元组
p = (1,2,3)
print(p)
t = (22,)
print(t)
print(3*t)
#tuple()将一个序列转化为元组
print(tuple('Python'))
#元组片操作与列表相同




