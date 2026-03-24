t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    
    idx , c = -1 , 0

    for i in range(n):
        c += int(s[i])
        if int(s[i]) % 2 == 1 and c % 2 == 0:
            idx = i
            break
    print(idx if idx == -1 else s[:idx+1])
    
    
