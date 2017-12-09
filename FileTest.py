with open(r'G:\PythonCore\File.txt','w+') as f:
    f.write('Hello, ')
    f.write('World!')
    line = f.readlines()
    print(line)
#with语句可以自动负责文件的关闭

f = open(r'G:\PythonCore\File.txt','r')
for l in f:
    print(l)

f.close()
