lst = [10, 20, 30, 40, 50]
indices = [0, 1, 2, 3, 4]
# res = enumerate(lst)
# print(list(res))

for i, val in enumerate(lst):
    print(i, val)

a = [10, 20, 30, 40, 50, 60]
b = [11, 22, 33, 44, 55, 66]
c = [101, 202, 303, 404, 505, 606]

for x, y, z in zip(a, b, c):
    print(x, y, z)



