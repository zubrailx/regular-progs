import re
file = open("file", encoding='utf-8')
string = file.readline()
a = []
t = 0
suma = 0
while string != "":
    a.append(re.match(r"^\d*", string).group(0))
    file.readline()
    file.readline()
    string = file.readline()
    t += 1
for i in a:
    suma += int(i)
print(suma/t)
