from multiprocessing import RLock, Pool, Lock

lock1 = RLock()
lock2 = RLock()


def dead_lock():
    lock1.acquire()
    print(1)
    sec()
    print(3)
    lock1.release()


def sec():
    lock2.acquire()
    print(2)
    lock2.release()


if __name__ == '__main__':
    dead_lock()
