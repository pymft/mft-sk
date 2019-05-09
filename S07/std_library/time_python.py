import time


def fact(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i

    return out


t1 = time.time()
res = fact(1000)
t2 = time.time()


print("Elapsed time : ", t2-t1)
# print(res)