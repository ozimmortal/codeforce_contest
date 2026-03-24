n = int(input())
st = input()

stack = []
re = 0

for s in st:
    if stack and stack[-1] == s:
        stack.pop()
        re += 1
    stack.append(s)
print(re)
