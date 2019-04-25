text = """Nothing can ever happen twice
in a consequence the sorry fact is
that we arrive here improvised 
and leave w/o the chance to practice   
"""

words = text.split()
length_of_words = []

for w in words:
    temp = len(w)
    length_of_words.append(temp)

print(length_of_words)
print(words)


new_list = zip(words, length_of_words)
print(list(new_list))