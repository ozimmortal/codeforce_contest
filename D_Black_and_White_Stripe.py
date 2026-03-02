t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().split()]
    s = input()

    l , ans = 0 , float('inf')
    w = 0

    for r in range(n):

        if s[r] == "W":
            w += 1
        
        while r - l + 1 > k:
            if s[l] == "W":
                w -= 1
            l += 1
        if r -l + 1 == k:
            ans = min(ans,w)
    print(ans)


