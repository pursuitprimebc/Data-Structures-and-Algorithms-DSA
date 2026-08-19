r, c = map(int, input().split())

cake = []
for i in range(r):
    cake.append(input())
    
evil_rows = [0] * r
evil_cols = [0] * c

for i in range(r):
    for j in range(c):
        if cake[i][j] == 'S':
            evil_rows[i] = 1
            evil_cols[j] = 1
            
eaten_cells = 0
for i in range(r):
    for j in range(c):
        if evil_rows[i] == 0 or evil_cols[j] == 0:
            eaten_cells += 1
            
print(eaten_cells)

