f = open('input.txt')
# f = open('C:/Users/Administrator/PycharmProjects/mft-sk/S07/file_manipulation/input.txt')
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/file_manipulation/    .
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/                      ..   ./..
#          C:/Users/Administrator/PycharmProjects/mft-sk/                          ../..
#          C:/Users/Administrator/PycharmProjects/                                 ../../..
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/                      ..
#          C:/Users/Administrator/PycharmProjects/mft-sk/S07/                      ..

text = f.read(10)
print(text)
text = f.read(10)
print(text)
