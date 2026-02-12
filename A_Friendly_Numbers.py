t = int(input())

for _ in range(t):
    n = int(input())

    ans = 0
    for y in range(n , n+100):
        s = 0
        x = y
        while x > 0:
            s += x % 10
            x //= 10
        if n == y - s:
            ans +=1
    print(ans)
            