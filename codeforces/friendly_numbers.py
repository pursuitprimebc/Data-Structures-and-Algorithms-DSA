t = int(input())
for i in range(t):
    x = int(input())
    count = 0
    for y in range(x,x+82):
        sum_of_y = 0
        y_str = str(y)
        for i in y_str:
            number = int(i)
            sum_of_y += number

        if (y-sum_of_y)==x:
            count += 1 

    
    print(count)