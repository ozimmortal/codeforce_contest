from collections import Counter
t = int(input())

for _ in range(t):

    w = input()
    p = int(input())
    res = ""
    c = 0
    
    for ch in w :
        c += ord(ch) - 96
    
    if c <= p:
        print(w)
        continue

    sw = sorted(w, reverse=True)
    rc = Counter()
    i = 0
    while c > p and i < len(w):
        c -= ord(sw[i]) -96
        rc[sw[i]] += 1
        i += 1
    res = []

    for ch in w:
        if rc[ch] !=0:
            rc[ch] -= 1
            continue
        res.append(ch)

        
    print("".join(res))

        

        

