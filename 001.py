def combinations(*argv):
    combs = 1
    for arg in argv:
        combs = combs * arg
    return combs


print(combinations(1, 2, 3, 4))
