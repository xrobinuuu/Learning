#
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Semaphore, get_ident


class RSemaphore:
    def __init__(self, value=1):
        self._active = {}
        self._semaphore = Semaphore(value)

    def acquire(self):
        current_thread = get_ident()
        if current_thread in self._active:
            self._active[current_thread] += 1
        else:
            self._semaphore.acquire()
            self._active[current_thread] = 0

    __enter__ = acquire

    def release(self):
        current_thread = get_ident()
        if current_thread not in self._active:
            raise KeyError("Cannot release a semaphore by another thread")
        elif self._active[current_thread] > 0:
            self._active[current_thread] -= 1
        else:
            del self._active[current_thread]
            self._semaphore.release()

    def __exit__(self, t, v, tb):
        self.release()


semaphore = RSemaphore(1)


def recursion_count(i, count):
    with semaphore:
        print(i, count)
        semaphore.acquire()
        time.sleep(0.5)
        if count > 0:
            return recursion_count(i, count - 1)


def main():
    pool = ThreadPoolExecutor(max_workers=10)
    for i in range(3):
        pool.submit(recursion_count, i, 3)


if __name__ == '__main__':
    main()
