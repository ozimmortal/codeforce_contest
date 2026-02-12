import sys

t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pos = 0
    first_hit = -1
    cycle = -1
    
    for i in range(n):
        pos += 1 if s[i] == 'R' else -1
        
        if first_hit == -1 and x + pos == 0:
            first_hit = i + 1
        
        if cycle == -1 and pos == 0:
            cycle = i + 1

    if first_hit == -1 or first_hit > k:
        print(0)
    elif cycle == -1:
        print(1)
    else:
        print(1 + (k - first_hit) // cycle)
