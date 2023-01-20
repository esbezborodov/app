str=input('ВВедите слова через пробел: ')
result=' '.join(i for i in str.split() if not any(c.isdigit() for c in i))
print(result)