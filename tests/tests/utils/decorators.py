from time import time, sleep
from selenium.common.exceptions import TimeoutException

def retry(click_retry):
    def func_retry(func):
        def wrapper(*args, **kwargs):
            for i in range(click_retry):
                try:
                    return func(*args, **kwargs)
                except TimeoutException:
                    if i >= click_retry - 1:
                        raise
        return wrapper
    return func_retry

def wait(method, error=Exception, timeout=3, interval=0.5, check=False, **kwargs):
    started = time()
    last_exception = None
    while time() - started < timeout:
        try:
            result = method(**kwargs)
            if check:
                if result:
                    return result
                last_exception = f"Method {method.__name__} returned {result}"
            else:
                return result
        except error as e:
            last_exception = e

        sleep(interval)

    raise TimeoutError(f"Method {method.__name__} timeout out in {timeout}sec with exception: {last_exception}")