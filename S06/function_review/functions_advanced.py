def my_sum(*args):
    print(args)
    # tup = (a, b, c, d, e)
    # return sum(args)



args_call = (1, 2, 3, 1000, 1)
# res = my_sum(1, 2, 3, 1000, 1)
res = my_sum(*args_call)


print(res)
