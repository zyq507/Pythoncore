__metaclass__ = type#指定使用新式类

class Person:
    def setName(self,name):
        self.name = name#self相当于C语言中的this指针
    def getName(self):
        return self.name
    def greet(self):
        print('Hello,%s' %self.name)

A = Person()
A.setName('ZYQ')
A.greet()

class Bird:
    song = 'Squaak!'
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()

birdsong = bird.sing#函数名只是一个标志，是可以随意替代的
birdsong()#相当于bird.sing()

#私有化的属性方式将会在之后介绍
class Secretive:
    def __inaccessible(self):
        print('You can\'t see it!')
    def accessible(self):
        self.__inaccessible()

Secret = Secretive()
#下面这一句是无法使用的，只能通过外部接口调用
#Secret.__inaccessible()
Secret.accessible()#可以引用inaccessible()
Secret._Secretive__inaccessible()#这个就可以用来使用

#超类
class Filter:
    def init(self):
        self.blocked = []
    def ffilter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class PPPFilter(Filter):
    def init(self):
        self.blocked = ['PPP']

K = PPPFilter()
K.init()
l = ['PPP','TT','DD','PPP','DP','PPP']
t = K.ffilter(l)
print(t)

