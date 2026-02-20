n , k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

if n == k :
    print(0)
elif k == 1:
    print(arr[-1] - arr[0])
else:
    v = []
    for i in range(1,n):
        v.append(arr[i - 1] - arr[i])
    v.sort()
    res = arr[n - 1] - arr[0]

    for i in range(k - 1):
        res += v[i]
    
    print(res)

