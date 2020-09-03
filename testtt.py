from collections import Counter


# def makeAnagrams(a, b):
#     a = a.lower()
#     b = b.lower()

#     a = list(a)
#     b = list(b)

#     a = sorted(a)
#     b = sorted(b)

#     countsA = {}
#     countsB = {}

#     toRemove = 0

#     for i in a:
#         if i not in countsA:
#             countsA[i] = 1
#         else:
#             countsA[i] += 1

#     for j in b:
#         if j not in countsB:
#             countsB[j] = 1
#         else:
#             countsB[j] += 1

#     for i in countsA:
#         if i in countsB:
#             toRemove += abs(countsA[i] - countsB[i])
#         else:
#             toRemove += countsA[i]

#     for j in countsB:
#         if j not in countsA:
#             toRemove += countsB[j]

#     return toRemove
#     # print(toRemove)


# a = 'bugexikjevtubidpulaelsbcqlupwetzyzdvjphn'

# b = 'lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk'


# makeAnagrams(a, b)
# #
# class SinglyLinkedListNode:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# node = SinglyLinkedListNode(1)
# node.next = SinglyLinkedListNode(2)
# node.next.next = SinglyLinkedListNode(2)
# node.next.next.next = SinglyLinkedListNode(3)


# def condense(head):
#     cur = head
#     dupes = {}
#     # dupes[head.data] = 1

#     while cur is not None:
#         if cur.data not in dupes:
#             dupes[cur.data] = 1
#         else:
#             dupes[cur.data] += 1

#         cur = cur.next

#     # node = SinglyLinkedListNode(head.data)
#     # cur = node
#     # headNode = node
#     singleNodes = []
#     for i in dupes.keys():
#         singleNodes.append(i)
#         # cur = cur.next

#     headCopy = SinglyLinkedListNode(head.data)
#     for j in singleNodes:
#         new_node = SinglyLinkedListNode(j)

#         if headCopy is None:
#             headCopy = new_node
#             return

#         last = headCopy
#         while (last.next):
#             last = last.next

#         last.next = new_node

#     return headCopy


# condense(node)


input = "foo(bar)baz(blim)boo"
# input2 = "foo(bar(baz))blim"


def reverseInParentheses(s):
    s = s.replace('(', '|(')
    s = s.replace(')', ')|')
    s = s.split('|')

    for i in range(len(s)):
        if '(' in s[i]:
            s[i] = s[i].replace(')', '')
            s[i] = s[i].replace('(', '')
            s[i] = s[i][::-1]

    solution = ''
    for i in s:
        solution += i

    return solution


reverseInParentheses(input)
