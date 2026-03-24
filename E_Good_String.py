n = int(input())
s = input()
res = []

for c in s:
    if len(res) % 2 == 1 :
        if res[-1] == c:
            res.pop()
    res.append(c)
    
if len(res) % 2 == 1:
    res.pop()
    
print(n - len(res))
print("".join(res))