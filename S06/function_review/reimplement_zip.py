def my_zip(*args):
    len_list = len(args[0])
    len_tuple = len(args)
    out = []
    for i in range(len_list):
        tmp = []
        for j in range(len_tuple):
            tmp.append(args[j][i])
        tmp = tuple(tmp)
        out.append(tmp)

    return out


x = [1, 2, 3, 4, 1, 2, 3]
y = [0, 9, 1, 1, 3, 3, 6]
z = [1, 3, 0, 2, 4, 6, 0]
res = my_zip(x, y, z, x, y, z)

print(res)
# [(1, 0), (2, 9), (3, 1), (4, 1)]
# my_zip(x, y, z)
# [(1, 0, 1), (2, 9, 3), (3, 1, 0), (4, 1, 2)]
