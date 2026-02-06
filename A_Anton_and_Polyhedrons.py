
collection = {
    "Tetrahedron" : 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron" :12,
    "Icosahedron":20
}
result = 0
n = int(input())

for _ in range(n):
    t = input()
    if t in collection:
        result += collection[t]
print(result)