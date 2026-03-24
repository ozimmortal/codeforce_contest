res = []
n , m = map(int, input().split())
o = 0
f = False
while n <= m:
    res.append(m)
    o += 1

    if n == m:
        f = True
        break

    if m %2 == 0:
        m //=2
    elif m%10 == 1:
        m //= 10
    else:
        break

if f:
    print("YES")
    print(o)
    print(*res[::-1])
else:
    print("NO")
    

    

