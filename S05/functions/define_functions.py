
f = lambda x: x ** 2
char_counter = lambda text: len(text)
word_counter = lambda text: len(text.split())
y = f(10)
print(y)


poem = "april is the cruelest month"
print(word_counter(poem), char_counter(poem))