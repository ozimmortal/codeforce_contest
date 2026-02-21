n, m = [int(x) for x in input().split()]

t = 0
r = []

for _ in range(n):
    o , c = [int(x) for x in input().split()]
    t += o
    r.append(o - c)

if t <= m:
    print(0)
else:
    r.sort(reverse=True)
    s = 0

    for rs in r:
        t -= rs
        s += 1
        if t <= m:
            print(s)
            break
    else:
        print(-1)


