phonebook = {'Alice':'2341','Beth':'9102','Cecil':'3258'}

items = [('name','FCK'),('age','21')]
d =dict(items)
print(d)
print(d['name'])#其中的key相当于索引
print(len(d))
print('age' in d)
d['job'] = 'worker'
print(d)
del d['job']
print(d)
k = 'my name is %(name)s, I\'m %(age)s years old'% d
print(k)#字典的key可以做为%s的说明符

x = {'key':'value'}
y = x
x.clear()
print(y)#clear方法会清空x关联的存储空间，y也映射到此存储空间，故亦空

#copy和deepcopy
aa = {'username':'admin','machines':['foo','bar','baz']}
bb = aa.copy()#shallow copy
bb['username'] = 'mlh'
bb['machines'].remove('bar')#原地修改浅复制的内容，原文也会改变
print(aa,'\n',bb)
#使用deepcopy可以解决问题

print({}.fromkeys(['a', 'bb']))#参数是一个list
print(dict.fromkeys(['f','g'],'Hello'))#可以添加一个缺省的参数

print(d.get('name'))#无key时，不会报错
print(d.get('job','N/A'))#可以添加一个参数来赋予缺省值的返回

print(list(d.items()))
print(list(d.keys()))

aaa = {}
aaa.setdefault('name','N/A')#setdefault可以在没有该key时设定默认值
print(aaa)#也可以同get方法在存在该key时获得该值
aaa['name'] = 'Boy'
print(aaa.setdefault('name','N/A'))

