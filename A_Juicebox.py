from collections import Counter
t = int(input())

for _ in range(t):
    n , k = map(int , input().split())
    c = [0] * k
    for _ in range(k):
        bi , ci =map(int,input().split())
        c[bi - 1] += ci
    c.sort(reverse=True)
    
    print(sum(c[:n]))