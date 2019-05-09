# r --> readable
# w --> writeable
# a --> append

# t --> text
# b --> bytes

# +

f = open("output.txt", mode='r+')
# text = f.read()
f.seek(10, 2)
f.write("hello")

# print(text)


