from collections import Counter
t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().split()]
    cards = [int(x) for x in input().split()]

    c = Counter(cards)

    res = 0
    keys = list(c.keys())
    for r in range(len(keys)):
        curr = 0
        x = keys[r]
        for _ in range(k):
            curr += c[x]
            x += 1
        
        res = max(res,curr)
    print(res)
            

    
