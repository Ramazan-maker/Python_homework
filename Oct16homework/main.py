import time

def measuretime(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print("Время выполнения: ",time.perf_counter_ns() - start_time)
        return res
    return wrapped

@measuretime
def func(first, second):
    return bin(int(first, 2) + int(second, 2))

print(func("111", "0000"))