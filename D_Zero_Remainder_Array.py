from collections import defaultdict
t = int(input())

for _ in range(t):
    n,k = (int(x) for x in input().split(" "))
    arr = [int(x) for x in input().split(" ")]

    freq = defaultdict(int)

    for  num in arr:
        
        r = num % k
        if r != 0:
            n = k - r
            freq[n] += 1

    if not freq : 
        print(0)
        continue

    max_moves = 0
    for n , f in freq.items():
        m = k * ( f -1) + n + 1
        max_moves =max(max_moves,m)
    print(max_moves)


