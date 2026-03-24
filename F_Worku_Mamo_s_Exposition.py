n , k = map(int, input().split())
arr = list(map(int, input().split()))

from collections import deque

maxdq = deque()
mindq = deque()
left = 0
res = []
maxl = 0
for right in range(n):
    
    while maxdq and arr[maxdq[-1]] <= arr[right]:
        maxdq.pop()
    
    while mindq and arr[mindq[-1]] >= arr[right]:
        mindq.pop()

    maxdq.append(right)
    mindq.append(right)

    while arr[maxdq[0]] - arr[mindq[0]] > k:
        left += 1
        if maxdq[0] < left:
            maxdq.popleft()
        if mindq[0] < left:
            mindq.popleft()
        
    curr = right - left + 1

    if curr > maxl:
        maxl = curr
        res = [(left + 1 , right + 1)]
    elif curr == maxl:
        res.append((left + 1, right + 1))

print(maxl, len(res))
for r in res:
    print(*r)