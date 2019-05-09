import urllib.request


f = urllib.request.urlopen('https://www.python.org')
text = f.read()
text_str = text.decode('utf-8')
print(text_str)
