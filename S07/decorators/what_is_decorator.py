def fun_weird(f):
    def out(x):

        res = f(x)

        return res
    return out



def echo(s):
    return s

new_len = fun_weird(len)
new_max = fun_weird(max)
val = new_len([1, 2, 3])
val = new_max([1, 2, 3])
print(val)
