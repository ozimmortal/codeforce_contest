t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().split()]
    m = [int(x) for x in input().split()]
    
    monsters = []
    for i, x in enumerate(m):
        r = x % k
        if r == 0:
            r = k
        monsters.append((-r, i))
    monsters.sort()

    print(*[ i + 1 for _ , i in monsters ])