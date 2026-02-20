from collections import Counter
t = int(input())

for _ in range(t):
    m, s = (int(x) for x in input().split())
    arr = [int(x) for x in input().split()]
    arrs = set(arr)
 
    ma = max(arrs) 
    cs= sum(arrs)

    n = ma
    while True:
        target = n * (n + 1) // 2
        ms = target - cs
        if ms== s:
            print("YES")
            break
        if ms > s:
            print("NO")
            break
        n += 1
