import threading
from time import ctime, sleep


loops = [4, 2]


def loop(nloop,nesc):
    print 'start loop', nloop, 'at:', ctime(), '\n'
    sleep(nesc)
    print 'loop', nloop, 'done at:', ctime(), '\n'


def main():
    print 'starting at:', ctime(), '\n'
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()

