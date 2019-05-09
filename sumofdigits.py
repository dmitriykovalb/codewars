def digital_root(n):
    # sum = 0
    # numstr = str(n)
    # numlist = list(numstr)
    # for i in numlist:
    #     sum += int(i)
    return sum(map(int, str(n)))


print(digital_root(141))
