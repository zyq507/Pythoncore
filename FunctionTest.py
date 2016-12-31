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
            
