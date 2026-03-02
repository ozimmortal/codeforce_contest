from collections import Counter
n , k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

l ,ans = 0 , 0 
c = Counter()
for r in range(n):

    c[arr[r]] += 1
    while len(c) > k:
        c[arr[l]] -= 1
        if c[arr[l]] == 0:
            del c[arr[l]]
        l += 1
    
    ans += r - l + 1
    
print(ans)
