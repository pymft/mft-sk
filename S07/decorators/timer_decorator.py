import time
import math


def timer(f):
    def f_decorated(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        print("Elapsed time : ", t2 - t1)

        return res
    return f_decorated


def tired(f):
    def f_decorated(*args, **kwargs):
        print("gonna start it in a minute")
        res = f(*args, **kwargs)
        time.sleep(2)
        return res
    return f_decorated


@timer
@tired
def fact(n):
    return math.factorial(n)


@timer
def fact_old(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i

    return out


num = 10000
res = fact(num)
print(res)
res = fact_old(num)
print(res)
