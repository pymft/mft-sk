lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = lambda a: a**2 -100*a + 0.2321
res = map(f, lst)

out_list = [a ** 2 for a in lst]
out_gen = (a ** 2 for a in lst)     # makes a generator not a tuple,
# print(out)

for x in out_gen:
    print(x)
