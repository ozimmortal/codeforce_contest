n , b = map(int, input().split())
a = map(int, input().split())

parity = {0 : 0 , 1 : 0}
c = []
for i in range(n-1):
    parity[i%2] += 1
    if parity[0] == parity[1]:
        c.append(i)

res = 0

for i in c:
    if b >= i:
        res +=1
        b -=i
    else:
        break
print(res)



