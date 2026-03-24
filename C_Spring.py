t = int(input())

for _ in range(t):
    d = list(map(int , input().split()))
    m = d[-1]
    res = [0]*3
    
    for i in range(1,m+1):
        for j in range(3):
            if i % d[j] == 0:
                res[j] += 1 
    print(*res)
a = "a"
a.s