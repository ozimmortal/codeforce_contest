t = int(input())

for _ in range(t):
    n = int(input())

    a ,b = 0 ,0
    c = 1
    r = n

    while r > 0:
        t = c if c <= r else r
        if c % 4 == 1 or c % 4 == 0:
            a += t
        else:
            b += t
        r -= t
        c += 1

    print(a, b)

            
        



