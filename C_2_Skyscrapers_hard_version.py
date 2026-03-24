n  = int(input())
floors = list(map(int,input().split()))
max_i = floors.index(max(floors))

left = []
right = []


# left 
c = max_i

for i in range(max_i, -1 , -1):
    left.append(min(floors[i] , c))