import math


# def distance(x, y):
#     return math.sqrt(x**2 + y**2)


def distance(x, y, norm=2, mode=100):
    print("mode --> ", mode)
    a = x ** norm + y ** norm
    b = a ** (1/norm)
    return b


print(distance(12, 5, norm=1))
print(distance(3, 4, mode=1000000))
