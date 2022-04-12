n = 0
while n < 10:
    if n == 3:
        n += 1
        continue
    if n == 6:
        n += 1
        pass
    print(n)
    n += 1