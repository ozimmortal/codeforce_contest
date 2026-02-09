n = int(input())
a = list(map(int, input().split()))

result = []

for i in range(n):
    count = 0
    for j in range(n):
        if a[j] > a[i]:
            count += 1
    result.append(count + 1)

print(*result)
