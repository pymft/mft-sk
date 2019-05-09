import math

def decorator(f):
    def out(*args, **kwargs):
        res = f(*args, **kwargs)
        return res
    return out


@decorator   # echo = decorator(echo)
def echo(s, n):
    return s


res = echo("Hello", 7)
print(res)

