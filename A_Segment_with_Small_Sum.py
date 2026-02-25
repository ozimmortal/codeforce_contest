n , s = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

ans , curr , l = 0 ,0
for r , num in enumerate(arr):
    curr += num
    while curr > s:
        curr -= arr[l]
        l += 1
    ans = max(ans,r -l + 1)
print(ans)
