t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    note = set()
    flag = False

    
    if n < 4:
        print("NO")
        
    else:
        i = 0
        while i < n-1:
            if s[i:i+2] in note:
                flag = True
                break
            else:
                note.add(s[i:i+2]) 
        
        if flag:
            print("YES")
        else:
            print("NO")

        
    

        
        