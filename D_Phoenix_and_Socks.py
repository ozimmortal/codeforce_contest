from collections import Counter
t = int(input())

for _ in range(t):
    n,l,r = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    cost = 0

    left = Counter(arr[:l])
    right = Counter(arr[l:])

    for color in list(left.keys()):
        m = min(left[color], right[color])
        left[color] -= m
        right[color] -= m
        l -= m
        r -= m

    if l > r:
        left, right = right, left
        l, r = r, l

    diff = r - l
    for color in right:
        while right[color] >= 2 and diff > 0:
            right[color] -= 2
            diff -= 2
            cost += 1
    
    cost += diff // 2
    remaining = sum(right.values())
    cost += remaining // 2

    print(cost)

