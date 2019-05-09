def tag_maker(tag):
    def decorator(f):
        def out(x):
            res = f(x)
            if type(res) == str:
                res = "<" + tag + ">" + res + "</" + tag + ">"
            return res

        return out

    return decorator


@tag_maker("span")
def echo(s):
    return s


print(echo("Hello"))
print(echo(10))
