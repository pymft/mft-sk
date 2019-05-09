f = open('input.txt')
text = f.read()
f.close()
n, c = text.split()
n = int(n)

f2 = open('output.txt', mode='w')
for i in range(1, n+1):
    f2.write(i*c)
    f2.write('\n')