import threading
from time import ctime, sleep

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop,nesc):
    print 'start loop', nloop, 'at:', ctime(), '\n'
    sleep(nesc)
    print 'loop', nloop, 'done at:', ctime(), '\n'


def main():
    print 'starting at:', ctime(), '\n'
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()
