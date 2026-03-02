n , k = [int(x) for x in input().split()]
nums = [[int(x) , i + 1 ] for i,x in enumerate(input().split())]
nums.sort(key=lambda x : x[0])

ans = []
s = 0

for n , i in nums:
    if  s + n > k:
        break
    else:
        s += n
        ans.append(i)

print(len(ans))
print(*ans)