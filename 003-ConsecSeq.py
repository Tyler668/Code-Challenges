def consecutive_combo(lst1, lst2):

    lst3 = lst1 + lst2
    lst3.sort()

    consecutive = True

    for i in range(len(lst3) - 1):
        if lst3[i+1] != lst3[i] + 1:
            consecutive = False
    return consecutive


print(consecutive_combo([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))
