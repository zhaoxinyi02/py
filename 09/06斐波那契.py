def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)
for n in range(1,16):
    print(f(n))