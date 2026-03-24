t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    
    stack = []

    for  i in nums[::-1]:
        while stack and stack[-1] < i:
            stack.pop()
        stack.append(i)
    print(len(stack))

    

