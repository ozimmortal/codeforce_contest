n = int(input())
arr = [int(x) for x in input().split()]

s = set(arr)

for i in range(1, n + 1):
    if i not in s:
        print(i)
