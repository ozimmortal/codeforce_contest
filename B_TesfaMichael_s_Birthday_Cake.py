n , k = map(int , input().split())
s = sorted(input())
stack = [s[0]]
i = 1
while i < n and len(stack) < k:
    if stack and abs(ord(stack[-1]) - ord(s[i])) > 1:
        stack.append(s[i])
    i+= 1

if len(stack) < k:
    print(-1)
else:
    t = 0
    for c in stack:
        t += ord(c) - ord('a') + 1
    print(t)




