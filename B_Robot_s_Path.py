n , k = [int(x) for x in input().split()]
road = input()

ob = True
p = 0
for  i in range(n -1):
    if road[i] == ".":
        p = i
    else:
        if i - p  >= k:
            ob = False
            break 
    
print("YES" if ob  else "NO")