from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el, end=' ')

from itertools import cycle
i = 0
for el in cycle("\nabc"):
    if i > 20:
        break
    print(el, end=' ')
    i += 1