lst = [(1, 9), (2, 99), (3, 0), (4, 8), (5, -106)]
# test = [9-1, 99-2, 0-3, 8-4, 6-5]
# test = [8, 97, -3, 4, 1]
f = lambda x: abs(x[1] - x[0])
res = max(lst, key=f)
print(res)

# res = max(test)
# ind = test.index(res)
# print(res, lst[ind])
