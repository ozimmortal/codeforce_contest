str = input()

if len(str) == 1:
    print(str)
else:
    arr = str.split("+")
    arr.sort()
    print("+".join(arr))