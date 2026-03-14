t = int(input())

for _ in range(t):
    n = int(input())
    a = set(list(map(int,input().split())))
    
    b  = sorted(a)
    l = 0
    ans = 0

    for r in range(len(a)):

        while b[r] - b[l] > n -1:
            l += 1
        ans = max(ans , r - l + 1)
    print(ans)


