def bold(f):
    def out(x):
        res = "<b>" + f(x) + "</b>"
        return res
    return out


def italic(f):
    def out(x):
        res = "<i>" + f(x) + "</i>"
        return res
    return out


@bold
@italic
def echo(s):
    return s


# echo = italic(echo)
# echo = bold(echo)

# echo = bold(italic(echo))

print(echo("hello"))
