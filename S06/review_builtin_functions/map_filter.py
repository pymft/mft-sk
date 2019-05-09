lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = lambda a: (a, a ** 2, a**3)

res = map(f, lst)

# print(list(res))

for x, y, z in res:
    print(x, '+', y, '+', z, '=', x+y+z)

