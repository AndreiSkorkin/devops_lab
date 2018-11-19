def loop(N):
    if 0 <= N <= 20:
        for i in range(N):
            print(i ** 2)
            i += 1
    else:
        return ("End")


if __name__ == '__main__':
    N = input("Enter number: ")
