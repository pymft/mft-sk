text = """Python is an interpreted, high-level, 
general-purpose programming language. 
Created by Guido van Rossum and first 
released in 1991, Python has a design 
philosophy that emphasizes code readability,
 notably using significant whitespace. 
 It provides constructs that enable clear 
 programming on both small 
and large scales. Wikipedia"""

vowels = []
consonants = []

words = text.split()
print(words)
# words
# occurances of the or The
#
for word in words:
    # if word[0] in "AEIOUaeiou":
    #     vowels.append(word)
    # else:
    #     consonants.append(word)


print(vowels)
print(consonants)