t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    sh = [0] * n
    p = True
    i = 0

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        if j - i == 1:
            p = False
            break

        for k in range(i, j - 1):
            sh[k] = k + 2 
            print(sh)
        print(j)
        sh[j - 1] = i + 1     
        i = j

    print(*sh if p else [-1])