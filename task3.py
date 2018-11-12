w, h = input().split()
w = int(w)
k = 0
h = int(h)
sq = []
count = int(input())
arr = [[0] * h for i in range(w)]
for i in range(count):
    square = [int(l) for l in input().split()]
    for i in range(square[0], square[2]):
        for j in range(square[1], square[3]):
            arr[i][j] = 1
for i in arr:
    for j in i:
        if j == 0:
            k += 1
print(k)
