
try:
    x = input('please input the first number: ')
    y = input('please input the second number: ')
    print(float(x)/float(y))
except (ZeroDivisionError, TypeError):#利用异常判断正确
    print('this second number can\'t be zero!')
except ValueError as e:#可以输出异常的对象
    print(e)
    print('this isn\'t a number')
#except语句还可以添加else
finally:#无论try except是否报错都会产生异常
    print('This is easy!')
    
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

Calc = MuffledCalculator()
print(Calc.calc('1+2'))
Calc.muffled = True
print(Calc.calc('2/0'))





    
