t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    a,b = map(int, input().split())

    min_dollar =[]
    cost_independent = (x + y) * a
    cost_joint = min(x, y) * b + abs(x - y) * a
    min_dollar.append(str(min(cost_independent, cost_joint)))

    print(*min_dollar)
