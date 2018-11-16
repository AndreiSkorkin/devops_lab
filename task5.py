n, m = map(int, input().split())
if 1 <= n <= 100000 and 1 <= m <= 100000:
    print("Type %r integers in array:" % (n))
    arr = input().split()
    print("Type %s integers in A set:" % (m))
    A = set(input().split())
    if len(A) != m:
        print("Wrong length! You'll get wrong result!")
    print("Type %s integers in B set:" % (m))
    B = set(input().split())
    if len(B) != m:
        print("Wrong length! You'll get wrong result!")
    result = 0
    for i in arr:
        if i in A:
            result += 1
        if i in B:
            result -= 1
    print(result)
else:
    print("error input")
