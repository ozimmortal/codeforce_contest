from collections import Counter
n , k = list(map(int,input().split()))

nums = list(map(int, input().split()))

l, m = 0 , 0
al , ar = 0 , 0
c = Counter()

for r in range(n):
    c[nums[r]] += 1

    while len(c) > k:
        c[nums[l]] -= 1

        if c[nums[l]] == 0:
            del c[nums[l]]
        l += 1
    
    if r - l + 1 > m:
        m = r - l + 1
        al = l
        ar = r
print(al + 1,ar + 1)