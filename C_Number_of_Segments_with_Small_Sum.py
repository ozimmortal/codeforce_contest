n , s = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

l ,res = 0 , 0
curr = 0
for r in range(n):
    curr += nums[r]
    while curr > s:
        curr -= nums[l]
        l += 1
    res += r -l + 1

print(res)