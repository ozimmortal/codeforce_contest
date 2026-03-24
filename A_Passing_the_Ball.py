t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    i = s.find("L")

    print(n if i == -1 else i + 1)

    