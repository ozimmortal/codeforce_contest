n = int(input())

arr = [int(x) for x in input().split()]
arr.sort()

day = 1

for  a in arr:
    if a >= day:
        day += 1
            
print(day - 1)

            