def solve():
    m = input()
    d = input()

    def cost(arr):
        g = 0
        for s in arr:
            g += 1 if s == "+" else -1
        return g

    g = cost(m)
    e, p = 0, 0

    def backtrack(path, i):
        nonlocal e, p

        if len(path) == len(d):
            if cost(path) == g:
                p += 1
            e += 1
            return

        for j in range(i, len(d)):
            s = d[j]
            if s == "?":
                for v in ["+", "-"]:
                    path.append(v)
                    backtrack(path, j + 1)
                    path.pop()
            else:
                path.append(s)
                backtrack(path, j + 1)
                path.pop()

    backtrack([], 0)
    print(p /e)

solve()