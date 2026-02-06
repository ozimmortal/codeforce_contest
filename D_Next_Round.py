n , k = (int(i) for i in input().split(" "))

score = [int(i) for i in input().split(" ")]

p = 0
for i in score:
    if i >= score[k - 1] and i > 0:
        p += 1
        
print(p)