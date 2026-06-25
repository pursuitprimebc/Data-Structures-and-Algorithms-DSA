num1 = input()
num2 = input()
new_num = ''
for i in range(len(num1)):
    if num1[i] == num2[i]:
        new_num += '0'
    else :
        new_num += '1'

print(new_num)