t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    res = 0

    arr.sort()
    for i in range(2 * n - 2 ,-1 , -2):
        res += min(arr[i],arr[i + 1])
    print(res)
