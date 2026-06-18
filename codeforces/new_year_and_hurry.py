n,k = map(int, input().split())
total_contest_time = (240-k)
solved = 0

for i in range(1,n+1):
    time = 5*i
    if total_contest_time >= time:
        total_contest_time -= time
        solved += 1

print(solved)  