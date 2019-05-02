# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# is_even = lambda x: x% 2==0
# f = lambda x: x ** 2
# out_list = [a ** 2 for a in lst if a % 2 == 0]

# out_list = [a**2 for a in range(10) if 2 < a <=


import math


def combination(n, m):
    numerator = math.factorial(n)
    denominator = math.factorial(m) * math.factorial(n - m)
    result = numerator / denominator
    return int(result)


out_list = [[combination(n, i) for i in range(n + 1)] for n in range(10)]

print(out_list)
