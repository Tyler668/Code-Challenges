# # Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# # (i.e., [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).

# # You are given a target value to search. If found in the array return its index, otherwise return -1.

# # You may assume no duplicate exists in the array.

# # Your algorithm's runtime complexity must be in the order of O(log n).

# # Example 1:

# # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# # Output: 4
# # Example 2:

# # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# # Output: -1


# def search(nums, target):
#     mid = len(nums) // 2
#     # print(mid, nums[mid])
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] > target:
#         lowerHalf


# nums = [4, 5, 6, 7, 0, 1, 2, 19]
# target = 0

# print(search(nums, target))


def double_char(txt):
    solution = ''
    for i in range(len(txt)):
        double = 2 * txt[i]
        solution += double

    return solution


print(double_char("Hello"))
