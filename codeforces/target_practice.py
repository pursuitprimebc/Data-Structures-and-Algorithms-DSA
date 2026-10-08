t_str = input().strip()
while not t_str:
    t_str = input().strip()
t = int(t_str)

for _ in range(t):
    score = 0
    rows_read = 0
    
    while rows_read < 10:
        row = input().strip()
        
        # Skip any stray empty lines between testcases
        if not row:
            continue
            
        # Check all 10 columns in the valid row
        for c in range(10):
            if row[c] == 'X':
                # Calculate minimum distance to the closest edge
                score += min(rows_read, 9 - rows_read, c, 9 - c) + 1
                
        rows_read += 1
        
    print(score)