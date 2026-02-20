t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().split()]
    arr = []

    for _ in range(n):
        arr.append([int(x) for x in input().split()])
    
    arr.sort()
    # print(arr)
    for a,b,c in arr:
        if a <= k <= b:
            k = max(k,c)
       
    print(k)
    