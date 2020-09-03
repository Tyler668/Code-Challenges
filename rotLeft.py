def rotLeft(a, d):

    newArr = [0] * d
    for i in range(d):
        newIndex = (int(i) + 1)
        a[i] = a[newIndex]
        print('ye')

    return newArr


print(rotLeft([1, 2, 3, 4], 6))
