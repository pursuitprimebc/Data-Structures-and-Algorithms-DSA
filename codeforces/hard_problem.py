t = int(input())
for i in range(t):
    m,a,b,c = map(int,input().split())
    seat_a = min(m, a)
    seat_b = min(m, b)
    rem_seats = (m - seat_a) + (m - seat_b)
    seat_c = min(rem_seats, c)
    total_seats = seat_a + seat_b + seat_c
    print(total_seats)
    

