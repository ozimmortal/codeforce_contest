t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    # max prefix sum for r
    best_r = 0
    s = 0
    for x in r:
        s += x
        best_r = max(best_r, s)
    
    # max prefix sum for b
    best_b = 0
    s = 0
    for x in b:
        s += x
        best_b = max(best_b, s)
    
    print(best_r + best_b)