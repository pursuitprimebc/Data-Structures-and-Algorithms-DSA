a = int(input())
b = int(input())
c = int(input())

val1 = a+b+c
val2 = a*b*c
val3 = a+b*c
val4 = a*b+c
val5 = (a+b)*c
val6 = a*(b+c)

highest = val1

if val2 > highest:
    highest = val2
if val3 > highest:
    highest = val3
if val4 > highest:
    highest = val4
if val5 > highest:
    highest = val5
if val6 > highest:
    highest = val6

print(highest)


