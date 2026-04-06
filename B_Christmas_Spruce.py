 
n = int(input())
p = [int(input()) for _ in range(n-1)]

children = [[] for _ in range(n+1)]
for i in range(2, n+1):
    parent = p[i-2]
    children[parent].append(i)

is_leaf = [False]*(n+1)
for i in range(1, n+1):
    if len(children[i]) == 0:
        is_leaf[i] = True
f = True

for i in range(1, n+1):

    if not is_leaf[i]:
        l = 0

        for c in children[i]:
            if is_leaf[c]:
                l += 1
        
        if l < 3:
            f = False
            break

print("Yes" if f else "No")

