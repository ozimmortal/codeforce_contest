s , n = [ int(x) for x in input().split()]
rounds = []
for _ in range(n):
    e , b = [ int(x) for x in input().split()]
    rounds.append([e,b])

rounds.sort()
will_pass = True

for e , b in rounds:
    if s > e :
        s += b
    else:
        will_pass = False
        break

print("YES" if will_pass else "NO")

