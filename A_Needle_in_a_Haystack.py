from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    t = input()

    tc  = Counter(t)
    de  = False

    for ch in s:
        if ch in tc:
            tc[ch] -= 1

            if tc[ch] == 0:
                del tc[ch]
        else:
            de = True
            break
    
    if de :
        print("Impossible")
    else:
        new_t = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for a in alphabet:
            new_t += a * tc[a]
        
        res = ""

        ptr1 , ptr2 = 0 , 0

        while ptr1 < len(s) and ptr2 < len(new_t):
            if s[ptr1] <= new_t[ptr2] :
                res += s[ptr1]
                ptr1 += 1
                
            else:
                res += new_t[ptr2]
                ptr2 += 1
                
        
        if ptr2 < len(new_t):
            res += new_t[ptr2:]
        
        if ptr1 < len(s):
            res += s[ptr1:]
        
        print(res)

            
        


