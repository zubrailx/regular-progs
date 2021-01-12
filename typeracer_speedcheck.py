import re

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

file = open("file", encoding='utf-8')
string = file.readline()
manyStrings = string
tries = 0
total = 0
date = ''
acc = 0
while string != '':
    x = re.search(r"(\d*)( \w{3}\s(.+)%.*?)(\w+\. \d\d, \d\d\d\d|today)", manyStrings)
    if x:
        if date == '':
            date = x.group(4)
        elif date != x.group(4):
            print("\nDate: " + date + '\n')
            print("Total tries = " + str(tries))
            print("Average accuracy = " + str(toFixed(acc/tries, 2)))
            print("Average typing speed = " + str(toFixed(total/tries, 2))+ "\n---------------------------------------")
            tries = 0
            total = 0
            acc = 0
            date = ""
            continue
        tries += 1
        total += int(x.group(1))
        acc += float(x.group(3))
        manyStrings = ''
    string = file.readline()
    manyStrings += string

# не хочу париться насчет красивого кода(
print("\nDate: " + date + '\n')
print("Total tries = " + str(tries))
print("Average accuracy = " + str(toFixed(acc / tries, 2)))
print("Average typing speed = " + str(toFixed(total / tries, 2)) + "\n---------------------------------------")
