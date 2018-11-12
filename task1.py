N = int(input())
i = 0
if 0 <= N <= 20:
    for i in range(N):
        print(i ** 2)
        i += 1
else:
    print("End")
