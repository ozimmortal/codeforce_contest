t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    ans = [arr[0]]

    for  i in range(1,n-1):
        if (arr[i] - arr[i -1]) * (arr[i + 1] - arr[i]) < 0:
            ans.append(arr[i])
    ans.append(arr[-1])
    print(len(ans))
    print(*ans)


    