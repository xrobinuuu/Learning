import time


def retry(max_attempts=3, wait_time=3):
    """
    重试函数
    max_attempts: 最大重试次数
    wait_time: 重试间隔时间
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"正在重试{attempts + 1} 错误原因: {e}")
                    attempts += 1
                    time.sleep(wait_time)
            print(f"最大重试次数{max_attempts}次结束")

        return wrapper

    return decorator


def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print('方法 {name} 耗时:'.format(name=func.__name__), end - start)
        return result

    return wrapper
