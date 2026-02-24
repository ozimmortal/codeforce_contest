n , m  = [int(x) for x in input().split()]

ptr1 , ptr2 = 0 , 0

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

final = []

while ptr1 < n and ptr2 < m:

    if arr1[ptr1] <= arr2[ptr2]:
        final.append(arr1[ptr1])
        ptr1 += 1
    else:
        final.append(arr2[ptr2])
        ptr2 += 1


for  i in range(ptr1,n):
    final.append(arr1[i])

for  i in range(ptr2,m):
    final.append(arr2[i])

print(*final)

