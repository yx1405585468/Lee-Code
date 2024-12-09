import sys

i = 0
test = {}
num = 0
for line in sys.stdin:
    i += 1
    if i == 1:
        num = int(line)
    else:
        line = int(line)

        test[line] = 0
        if i > num:
           for i in sorted(test.keys()):
               print(i)
