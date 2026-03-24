n = int(input())
res = 0
for _ in range(n):
    a = [ int(x) for x in input().split()]
    s = a[0] + a[1] + a[2]
    if s >= 2: res += 1
print(res)