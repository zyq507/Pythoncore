__metaclass__ = type
#属性
class Rect:
    def __init__(self, size=(1,1)):
        self.Width, self.Height = size
    def setSize(self,size):
        self.Width, self.Height = size
    def getSize(self):
        return self.Width, self.Height
    size = property(getSize, setSize)


rect = Rect((4,1))
rect.size = (1,5)
print(rect.size)
#静态方法和类方法：（不是很常用）    
class Myclass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)

Myclass.smeth()
Myclass.cmeth()

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b =  self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()
for x in fibs:
    if x>100:
        print(x)
        break

class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value>10: raise StopIteration
        return self.value
    def __iter__(self):
        return self

it = TestIterator()
k = list(it)
print(k)

