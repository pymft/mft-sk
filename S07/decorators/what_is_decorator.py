def fun_weird(f):
    # out = len
    out = lambda x: f(x)
    return out


new_len = fun_weird(len)
def new_len(x):
    return len(x)
new_max = fun_weird(max)
new_min = fun_weird(min)

val = new_len([1, 2, 3])
print(val)
