t = int(input())
for i in range(t):
    n = int(input().strip())
    if n % 3 == 0:
        print("Second")
    else:
        print("First")


''' case 1 - not multiple of 3
if the number is  exactly 1 above a multiple of 3 (Vanya subtracts 1) or if it is exactly 1 below a multiple of 3 (Vanya adds 1). Vanya wins on the first move s he starts th e game.

but , case 2 - multiple of 3
Vanya has to change the number from the multiple of 3. when vova plays , he will simply reverse Vanya's move. This brings the number right back to a multiple of 3. and vanya will again stuck with the  same process.
'''
