import sys
sys.setrecursionlimit(10**7)

t = int(input())

def solve(n, m):
    if n == m:
        return True
    if n < m or n % 3 != 0:
        return False
    x = n // 3
    return solve(x, m) or solve((2 * x) , m)

for _ in range(t):
    n, m = map(int, input().split())
    print("YES" if solve(n, m) else "NO")