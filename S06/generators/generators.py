def fib(n):
    i = 0
    a, b = 1, 1
    while i < n:
        i += 1
        a, b = b, a + b
        yield b


gen = fib(10)
v1 = next(gen)
v2 = next(gen)
v3 = next(gen)
v4 = next(gen)
v5 = next(gen)

for i in gen:
    print(i)
#
# 1  1
# 2  1 1
# 3  1 1 1
# 4  1 1 1 1
# 5  1 1 1 1 1
# 6  1 1 1 1 1 1
# 7  1 1 1 1 1 1 1
# 8  1 1 1 1 1 1 1 1
# 9  1 1 1 1 1 1 1 1 1
#
# 1  1
# 2    1
# 3      1
# 4        1
# 5          1
# 6            1
# 7              1
# 8                1
# 9                  1
