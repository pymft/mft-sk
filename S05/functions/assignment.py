def fact(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i

    return out


def combination(m, n):
    res = fact(m) / (fact(m-n) * fact(n))
    return int(res)


def pascal_row(n):
    out = []
    for i in range(n+1):
        temp = combination(n, i)
        out.append(temp)

    return out


def pascal(rows):
    out = []
    for i in range(1, rows+1):
        temp = pascal_row(i)
        out.append(temp)

    return out

res= pascal(6)
print(res)