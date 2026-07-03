n_str = input()
count = 0
current_letter = ''

for i in n_str:
    if i == current_letter:
        count += 1
    else:
        current_letter = i
        count = 1
    if count >= 7:
        print('YES')
        exit()

print('NO')