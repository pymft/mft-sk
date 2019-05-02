lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f_pow2 = lambda t: t ** 2
f_even = lambda x: x % 2 == 0

evens = filter(lambda x: x % 2 == 0, lst)
res = map(lambda t: t ** 2, evens)
map(f, lst)
# [f(1), f(2), f(3), f(4), f(5), f(6), f(7), f(8), f(9)]

print(list(res))


def my_map(fun, inp):
    out = []
    for i in inp:
        out.append(fun(i))
    return out


def my_filter(fun, inp):
    out = []
    for i in inp:
        if fun(i):
            out.append(i)
    return out
