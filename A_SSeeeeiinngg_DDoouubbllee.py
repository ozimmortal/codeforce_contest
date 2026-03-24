from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    c = Counter()

    for i in range(len(s)):
        c[s[i]] += 2
    res = ""

    for k in c:
        res += k * (c[k] // 2)

    
    print(res + res[::-1])
     