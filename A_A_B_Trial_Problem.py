n = int(input())

for _ in range(n):
    a , b = (int(n) for n in input().split(" "))
    print(a + b)