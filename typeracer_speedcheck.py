import re
file = open("file", encoding='utf-8')
string = file.readline()
tries = 0
total = 0
while string != "":
    x = re.match(r"^\d*(?= WPM| CPM)", string)
    if x:
        total += int(x.group(0))
        tries += 1

    string = file.readline()

print(total/tries)
