
t = int(input())
s = input()

if t == 1 or len(set(s)) < t:
    print("Yes")
else:
    print("No")