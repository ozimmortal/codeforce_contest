from collections import Counter
t = int(input())

for _ in range(t):
    n,l,r = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    cost = 0

    left = Counter(arr[:l])
    right = Counter(arr[l:])

    for color in list(left.keys()):
        if color in right:
            m = min(left[color], right[color])
            left[color] -= m
            right[color] -= m
            l -= m
            r -= m

    if l > r:
        left, right = right, left
        l, r = r, l

    diff = (r - l) // 2
    p= 0
    for color in right:
        p += right[color] // 2
    m = min(diff,p)
    cost = diff + (l + r) // 2 - m
    

    print(cost)

