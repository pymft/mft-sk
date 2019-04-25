# f = lambda x : x ** 2
def f(x):
    res = x ** 2
    res = res + x ** 3
    return res


y = f(10)
print(y)