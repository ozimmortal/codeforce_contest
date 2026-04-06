h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]

# build hor and ver
hor = [[0]*w for _ in range(h)]
ver = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if j+1 < w and grid[i][j] == '.' and grid[i][j+1] == '.':
            hor[i][j] = 1
        if i+1 < h and grid[i][j] == '.' and grid[i+1][j] == '.':
            ver[i][j] = 1

# prefix sums
prefH = [[0]*(w+1) for _ in range(h+1)]
prefV = [[0]*(w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        prefH[i][j] = (
            hor[i-1][j-1]
            + prefH[i-1][j]
            + prefH[i][j-1]
            - prefH[i-1][j-1]
        )
        prefV[i][j] = (
            ver[i-1][j-1]
            + prefV[i-1][j]
            + prefV[i][j-1]
            - prefV[i-1][j-1]
        )

def query(pref, r1, c1, r2, c2):
    return (
        pref[r2][c2]
        - pref[r1-1][c2]
        - pref[r2][c1-1]
        + pref[r1-1][c1-1]
    )

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    
    # horizontal
    h_count = query(prefH, r1, c1, r2, c2-1) if c1 <= c2-1 else 0
    
    # vertical
    v_count = query(prefV, r1, c1, r2-1, c2) if r1 <= r2-1 else 0
    
    print(h_count + v_count)