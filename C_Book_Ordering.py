n = int(input())
arr = []
for _ in range(n):
    w , h = [int(x) for x in input().split()]
    s = [w, h] if w <= h else [h , w]
    arr.append(s)
maxh = arr[0][1]
f = True
for  i in range(1,n):
    if maxh >= arr[i][0] or maxh >= arr[i][1]:
        maxh = arr[i][1] if arr[i][1] <= maxh else arr[i][0]
    else:
        f = False
        break
print("YES" if f  else "NO")



