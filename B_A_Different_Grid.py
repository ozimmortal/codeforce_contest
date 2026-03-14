t = int(input())

for _ in range(t):
    n , m = map(int , input().split())

    board = [[] for _ in range(n)]
    for i in range(n):
        board[n -1 - i] = list(map(int, input().split()))[::-1]

    if n % 2 == 1:
        board[n // 2] ,board[0] = board[0] ,  board[n // 2]
    if m % 2 == 1:
        board[n//2][m//2],board[n//2][0] = board[n//2][0] ,board[n//2][(m//2)]
    
    if n * m <= 1:
        print(-1)
        continue
    for b in board:
        print(*b)
    