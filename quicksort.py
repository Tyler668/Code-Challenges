# Divide and conquer

# This is a recursive algorithm
# When writing a recursive algorithm/ implementation, think;
# 1. What's our base case(s)? What kills the recursion?
# 2. If we aren't in the base case, how are we slowly moving towards it?
# 3. monky 



def partition(data, start, end):
    # Pick the first element in data as our pivot
    pivot = data[start]

    i = start + 1
    j = start + 1

    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i+=1 
        j+=1

    data[start], data[i-1] = data[i-1], data[start]

    # Return index of the pivot
    return i-1
 

def quicksort(data, start = 0, end = None):
    if end is None :
        end = len(data) - 1 

    # Base case
    if len(data) == 0:
        return data

    # Returns the index of the pivot
    index = partition(data, start, end)

    # Qs call for everything to the left of the pivot
    quicksort(data, start, index - 1)

    # Qs call for everything to the right of the pivot
    quicksort(data, index+1, end)

    # left, pivot, right = partition(data)

    # return quicksort(left) + [pivot] + quicksort(right)


test = [2,3,54,6,2,5,6547,3,23,42,6,3412,4,3,2,2,3,5476,123,254,7,24]
print(quicksort(test))
