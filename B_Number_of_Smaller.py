n , m = [int(x) for x in input().split()]

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

ans = []

l = 0
for i in range(m):
    while l < n and arr1[l] < arr2[i]:
        l += 1
    ans.append(l)

print(*ans)

