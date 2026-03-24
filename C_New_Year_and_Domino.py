row , col = map(int,input().split())

prefix = [[0] * (col + 1) for _ in range(row + 1) ]

for r in range(1, row + 1):
    board = [1 if x == "." else - 1 for x in input()]
    for c , p in enumerate(board):
        c = c + 1
        prefix[r][c] = p + prefix[r-1][c] + prefix[r][c -1] - prefix[r-1][c-1]

q = int(input())

print(prefix)
for _ in range(q):
    r1,c1,r2,c2 = map(int,input().split())
    ans = prefix[r2][c2] + prefix[r1-1][c1-1] - prefix[r1-1][c2] - prefix[r2][c1-1]
    print(ans)
    

