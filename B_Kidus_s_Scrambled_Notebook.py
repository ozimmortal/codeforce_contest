t = int(input())

for _ in range(t):
    s = input()

    a = 0
    b = 0

    i = 1
    n = len(s) 
    
    if n == 1:
        print(-1)
        continue

    while i < n:
        if int(s[i]) != 0 and int(s[i:]) > int(s[:i]):
            a = s[:i]
            b = s[i:]
            break
        i += 1
    if not a or not b:
        print(-1)
    else:
        print(a,b)








        
