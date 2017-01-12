__metaclass__ = type

class Point:
    def __init__(self, x=1, y=1):
        self.loc = dict(X = x,Y = y)
    def introduce(self):
        print('This is a point')
    def showPoint(self):
        self.introduce()
        print('The losation is (%s, %s)'
              %(str(self.loc.get('X')),str(self.loc.get('Y'))))
        
point = Point(2,2)
point.showPoint()

class Circle(Point):
    def __init__(self, x=1, y=1, r=1):
        super(Circle, self).__init__(x,y)#super函数使用的是自己
        self.radius = r
    def introduce(self):#重写了introduce函数
        print('This is a circle')
    def showCircle(self):
        self.showPoint();#此处记得有self
        print('The radius is %s'%str(self.radius))

circle = Circle(2,3,6)
circle.showCircle()

def checkIndex(key):
    if not isinstance(key,int):raise TypeError
    if key < 0:raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):#构造方法
        self.start = start
        self.step = step
        self.changed = {}
    def __getitem__(self,key):#用来获得列表上的值
        checkIndex(key)
        try:return self.changed[key]
        except KeyError:
            return self.start + key*self.step
    def __setitem__(self,key,value):#用来设置列表上的值
        checkIndex(key)
        self.changed[key] = value

s = ArithmeticSequence(1,2)
print(s[4])
s[4] = 2
print(s[4])
print(s[5])

class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.count = 0
    def __getitem__(self,index):
        self.count += 1#记录访问的次数
        return super(CounterList,self).__getitem__(index)
        #返回相应的索引值

c1 = CounterList(range(10))
r = c1[3] + c1[5]
print(c1.count)

#属性：


