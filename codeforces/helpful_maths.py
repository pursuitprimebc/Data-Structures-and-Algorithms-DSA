s= input().split('+')
count_1 = 0
count_2 = 0
count_3 = 0

for i in range(len(s)):
    if s[i] == '1':
        count_1 += 1
    elif s[i] == '2':
        count_2 += 1
    elif s[i] == '3':
        count_3 += 1
operation = ''
for i in range(count_1):
    operation += '1+'
for i in range(count_2):
    operation += '2+'
for i in range(count_3):
    operation += '3+'

print(operation[:-1])