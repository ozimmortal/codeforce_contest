n = int(input())

x , y , z = 0 , 0 , 0

for _ in range(n):
    a = list(map(int, input().split()))
    x += a[0]
    y += a[1]
    z += a[2]
if x or y or z:
    print("NO")
else:
    print("YES")

