from typing import List


class listNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def foo(self):
        curr = self
        res = str(self.val)
        while curr.next:
            curr = curr.next
            res += " " + str(curr.val)
        return res


def modifyLL(head):
    def findLast(head):
        curr = head
        while curr.next and curr.next.next:
            curr = curr.next

        return curr, curr.next

    curr = head
    while curr.next and curr.next.next:
        secondL, last = findLast(curr)
        temp = curr.next
        curr.next = last
        secondL.next = None
        curr.next.next = temp
        curr = curr.next.next

    return head

def buildLL(lst):
    head = listNode(lst[0])
    curr = head
    for i in range(1, len(lst)):
        curr.next = listNode(lst[i])
        curr = curr.next

    return head

def buildLst(n):
    res = []
    for i in range(n):
        res.append(i)
    return res


lst = buildLst(100000)
head = buildLL(lst)
print(head.foo())
print(modifyLL(head).foo())