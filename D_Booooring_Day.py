t = int(input())

for _ in range(t):
    n , ll , rl = [int(x) for x in input().split()]
    cards = [int(x) for x in input().split()]
    ro = 0
    curr = 0
    l = 0
    for r in range(n):
        if curr < ll:
            curr += cards[r]
        
        while curr > rl:
            curr -= cards[l]
            l += 1

        
        if  ll <= curr  <= rl:
            ro += 1
            curr = 0
            l =  r + 1
        
        
    print(ro)
