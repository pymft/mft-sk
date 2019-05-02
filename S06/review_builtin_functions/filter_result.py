lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

is_even = lambda x: x % 2 == 0

res = filter(is_even, lst)
print(list(res))