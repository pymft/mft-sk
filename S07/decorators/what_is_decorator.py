def fun_weird(f):
    def out(x):
        res = "\033[31;1m" + str(f(x)) + "\033[0m"
        return res

    return out


def echo(s):
    return s


echo_new = fun_weird(echo)
res = echo_new("hello")
print(res)

new_len = fun_weird(len)
print(new_len([1, 2, 3, 43]))
