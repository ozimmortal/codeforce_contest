t =  int(input())

for _ in range(t):
    s = input()

    if len(s) <= 3:
        print("NO")
    else:
        
        f = False
        for i in range(1,len(s)//2):
            if s[i] != s[i-1]:
                f= True
                break
        print("YES" if f else "NO")
