# 2. Add Two Numbers
#
# Description:
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for single-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val + l2.val
        carry = val // 10

        return ListNode(0)


def main():
    sol_input = [2, 7, 11, 15], 9
    expect_output = [0, 1]
    sol_output = Solution().addTwoNumbers([2, 7, 11, 15], 9)

    print(f'Your input:\t{sol_input}')
    print(f'Output: \t{sol_output}')
    print(f'Expected: \t{expect_output}')

    assert sol_output == expect_output
