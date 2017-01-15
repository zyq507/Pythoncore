#八皇后问题超级难。。。
import random
#冲突定义函数:
#state长度代表行数，每个元素代表相应行的列数。
def conflict(state, nextX):
    nextY = len(state)       #列出已有几行确定了皇后的位置
    for i in range(nextY):   #寻找每行中皇后的位置
        if abs(state[i]-nextX) in (0,nextY-i):#是否在同一列或对角线上
            return True
    return False
#好难想啊！！
def queens(num=8, state=()):
    for pos in range(num):  #遍历每一行的每个位置
        if not conflict(state,pos):
            if len(state) == num-1:#只剩最后一个的情况下
                yield (pos,)#这个用来最后加到result上（返回只有在num = 1时）
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result#真正的返回值
#图形化输出8皇后问题:
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '.'*(pos)+'X'+'.'*(length-pos-1)
    for pos in solution:#自动换行
        print(line(pos))

prettyprint(random.choice(list(queens(8))))
