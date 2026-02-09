t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if n ==4 and s != "2025":
        print(0)
        continue
    elif n == 4 and s == "2025":
        print(1)
        continue
    
    tracker  = 0
    for i in range(n-1):
        # print(s[i:i+4])
        if s[i:i+4] == "2025":
            tracker+=1
        elif s[i:i+4]  == "2026":
            tracker = 0
            break
    if tracker>0:
        print(1)
    else:
        print(0)
