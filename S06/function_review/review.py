import math


def combination(n, m):
    numerator = math.factorial(n)
    denominator = math.factorial(m) * math.factorial(n - m)
    result = numerator / denominator
    return str(int(result)).center(6)


def pascal_row(n):
    row = []
    for i in range(n + 1):
        val = combination(n, i)
        row.append(val)
    return row


def pascal(rows):
    res = []
    for i in range(rows + 1):
        current_row = pascal_row(i)
        res.append(current_row)
    return res


res = pascal(15)

for r in res:
    row = ''.join(r)
    print(row.center(100))
    # print(*r, sep='\t')
