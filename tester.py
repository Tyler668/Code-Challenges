def threeNumberSum(arr, target):
    matches = []
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    validSum = [arr[i], arr[j], arr[k]]
                    validSum.sort()
                    if validSum not in matches:
                        matches.append(validSum)

    matches = sorted(matches, key=sorted)
    return matches


print('Sums', threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20))
