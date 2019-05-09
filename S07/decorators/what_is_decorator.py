import math

def decorator(f):
    def out(x):

        res = f(x)

        return res

    return out


@decorator   # echo = decorator(echo)
def echo(s):
    return s


@decorator
def fact(n):
    return math.factorial(n)

# echo = decorator(echo)

res = echo("Hello")
print(res)


print(fact(5))
