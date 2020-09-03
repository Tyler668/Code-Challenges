class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeKthNode(head, k):
    nodeIndeces = {}
    i = 0

    cur = head
    while cur is not None:
        nodeIndeces[i] = cur
        cur = cur.next
        i += 1
    # print('I', i)
    if k > i:
        toRemove = None
    elif k > 0:
        toRemove = i - k
    elif k < 0:
        toRemove = k * -1

    # print(nodeIndeces)
    if toRemove != None:

        if nodeIndeces[toRemove] == head:
            head = head.next
            nodeIndeces[toRemove].next = None
        else:
            if nodeIndeces[toRemove].next is not None:
                nodeIndeces[toRemove - 1].next = nodeIndeces[toRemove+1]
            else:
                nodeIndeces[toRemove - 1].next = None

    return head

    # print('Original')
    # cur = head
    # while cur is not None:
    #     print(cur.val)
    #     cur = cur.next

    # print('Removed')
    # cur = head
    # while cur is not None:
    #     print(cur.val)
    #     cur = cur.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(8)
l1.next.next.next.next = ListNode(11)
# l1.next.next.next.next.next = ListNode(9)
removeKthNode(l1, 1)

# if nodeIndeces[toRemove - 1] in nodeIndeces and nodeIndeces[toRemove + 1] not in nodeIndeces:
#     # nodeIndeces[toRemove].next = None
#     nodeIndeces[toRemove - 1].next = None
# if nodeIndeces[toRemove - 1] in nodeIndeces and nodeIndeces[toRemove + 1] in nodeIndeces:
#     nodeIndeces[toRemove - 1].next = nodeIndeces[toRemove + 1]
