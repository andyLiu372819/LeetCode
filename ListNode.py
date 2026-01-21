class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if not head or not head.next:
        return head
    prev = ListNode()
    curr = head
    while curr and curr.next:
        prev.next = curr.next
        curr.next = prev.next.next
        prev.next.next = curr
        prev = curr
        curr = curr.next


def construct(lis):
    head = ListNode(lis[0], None)
    curr = head
    i = 1
    while i < len(lis):
        curr.next = ListNode(lis[i], None)
        curr = curr.next
        i += 1
    return head


def spell(head):
    curr = head
    print(curr.val)
    while curr.next:
        curr = curr.next
        print(curr.val)


if __name__ == "__main__":
    head = construct([1, 2, 3, 4])
    spell(head)
    swapPairs(head)
    spell(head)