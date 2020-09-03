def giveTrips(arr, target):
    matches = {}
    valid = []
    arr.sort()
    for i in range(0, len(arr) - 2):
        for j in range(1, len(arr) - 1):
            for k in range(2, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    validSum = [arr[i], arr[j], arr[k]]
                    validSum.sort()
                    if validSum not in matches:
                        matches[validSum] = target
                        valid.append(validSum)

    matches = sorted(matches, key=sorted)
    return matches


# def giveTrips2(arr, target):


def findTriplets(arr, Sum):
    n = len(arr)
    matches = []
    for i in range(n - 1):

        # Find all pairs with Sum equals
        # to "Sum-arr[i]"
        s = dict()
        for j in range(i + 1, n):
            x = Sum - (arr[i] + arr[j])
            if x in s.keys():

                validSum = [x, arr[i], arr[j]]
                validSum.sort()
                # if validSum not in matches:
                matches.append(validSum)
            else:
                s[arr[j]] = 1
        # matches = sorted(matches, key=sorted)

        return matches


# Driver code
arr = [0, -1, 2, -3, 1]
Sum = -2
n = len(arr)
print(findTriplets(arr, Sum))


arr = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(findTriplets(arr, target))
