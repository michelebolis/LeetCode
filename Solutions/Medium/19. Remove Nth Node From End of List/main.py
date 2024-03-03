from solution import Solution, ListNode
def toStringListNode(node) :
    if node is None : return "[]"
    toPrint = "["
    while node is not None :
        toPrint += str(node.val) + " "
        node = node.next
    toPrint = toPrint[:len(toPrint) - 1]
    toPrint += "]"
    return toPrint
case1 = ListNode(1)
case1.next = ListNode(2)
next = case1.next
next.next = ListNode(3)
next = next.next
next.next = ListNode(4)
next = next.next
next.next = ListNode(5)
next = next.next
print("from", toStringListNode(case1), "remove", 2, "-->", toStringListNode(Solution.removeNthFromEnd(None, case1, 2)))
case2 = ListNode(1)
print("from", toStringListNode(case2), "remove", 1, "-->", toStringListNode(Solution.removeNthFromEnd(None, case2, 1)))
case2.next = ListNode(2)
print("from", toStringListNode(case2), "remove", 1, "-->", toStringListNode(Solution.removeNthFromEnd(None, case2, 1)))