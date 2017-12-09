import thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nesc, lock):
    print 'start loop', 'nloop', 'at:', ctime(),'\n'
    sleep(nesc)
    print 'loop', nloop, 'done at:', ctime(),'\n'
    lock.release()


def main():
    print 'starting at:', ctime(),'\n'
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print 'all done at:', ctime()


if __name__ == '__main__':
    main()