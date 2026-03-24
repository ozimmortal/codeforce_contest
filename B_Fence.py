n , k = map(int , input().split())

h = list(map(int,input().split()))
prefix  = [h[0]]

for i in range(1,n):
    prefix.append(prefix[i - 1]+ h[i])

minH = prefix[0 + k - 1] - prefix[0] + h[0]
idx = 1
for i in range(1, n - k  + 1):
    t = prefix[i + k - 1] - prefix[i] + h[i]
    if t < minH:
        minH = t
        idx = i + 1

print(idx)
