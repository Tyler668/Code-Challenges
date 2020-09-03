# # You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# # You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# # Example:

# # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# # Output: 7 -> 0 -> 8
# # Explanation: 342 + 465 = 807.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

#         l1_arr = []
#         l2_arr = []

#         cur = l1
#         while cur is not None:
#             l1_arr.append(cur.val)
#             cur = cur.next

#         cur = l2
#         while cur is not None:
#             l2_arr.append(cur.val)
#             cur = cur.next

#         l1_arr.reverse()
#         l2_arr.reverse()

#         num1 = ''
#         num2 = ''

#         for digit in l1_arr:
#             num1 += str(digit)

#         for digit in l2_arr:
#             num2 += str(digit)

#         sum = int(num1) + int(num2)

#         sumArr = list(map(int, str(sum)))
#         sumArr.reverse()

#         cur = ListNode(sumArr[0])

#         for i in range(len(sumArr)):
#             cur.next = ListNode(sumArr[i + 1])
#             cur = cur.next

#         return cur


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(6)
# l1.next.next.next = ListNode(8)

# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(5)
# l2.next.next.next = ListNode(7)

# sol = Solution()
# sol.addTwoNumbers(l1, l2)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, l1, l2):
        nodeSet = []
        cur = l1
        while cur is not None:
            nodeSet.append(cur)
            cur = cur.next

        cur = l2
        while cur is not None:
            nodeSet.append(cur)
            cur = cur.next

        nodeSet = sorted(nodeSet, key=lambda item: item.val)

        for i in range(len(nodeSet) - 1):
            nodeSet[i].next = nodeSet[i+1]

        print('Nodeset sorted', nodeSet[0].val)
        return nodeSet[0]


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

l2 = ListNode(0)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(7)

# print('L1', l1)

# print('L2', l2)

l1.mergeTwoLists(l1, l2)
