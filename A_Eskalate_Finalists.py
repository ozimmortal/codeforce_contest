k = int(input())

arr = list(map(int, input().split()))

m  = max(arr)
d = m - 25

print(d if d > 0 else 0)


