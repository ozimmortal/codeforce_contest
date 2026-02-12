r1,c1 =  0 ,0

for i in range(5):
    for j,x in enumerate(input().split()):
        x = int(x)
        if x == 1:
            r1 = i + 1
            c1 = j + 1

print(abs(3-r1) + abs(3 - c1))

