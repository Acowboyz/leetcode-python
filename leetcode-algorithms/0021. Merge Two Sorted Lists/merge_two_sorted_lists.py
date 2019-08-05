# 21. Merge Two Sorted Lists
#
# Description:
#
# Merge two sorted linked lists and return it as a new list. The new list should
# be made by splicing together the nodes of the first two lists.
#
#
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        dump = ListNode(None)
        prev = dump

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1:
            prev.next = l1

        if l2:
            prev.next = l2

        return dump.next

    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            print(l1.val, l2.val)
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1
        else:
            print(l1.val, l2.val)
            l2.next = self.mergeTwoListsRecursive(l1, l2.next)
            return l2

# TODO: need to implement the utility to create lined list
