n = int(input())
width = len(bin(n)) - 2
if 1 <= n <= 99:
    for i in range(1, n + 1):
        print(
            str(int(i)).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].title().rjust(width),
            bin(i)[2:].rjust(width))
else:
    print("End")
