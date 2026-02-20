
n = int(input())

arr  = []

for i in range(n):
    a ,b  = [int(x) for x in input().split()]
    arr.append([a,b,i + 1])

a , b = -1,-1


arr = sorted(arr , key= lambda x: x[1] )
print(arr)

for i in range(len(arr)-1):
    if arr[i][0] >= arr[i + 1][0] and arr[i][1] <= arr[i + 1][1]:
        a , b = arr[i][2] , arr[i + 1][2] 
        break

print(a,b)
