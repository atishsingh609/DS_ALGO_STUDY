"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""

#
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)
        list_1 = []
        list_2 = []
        ptr_1 = l1
        ptr_2 = l2
        while ptr_1:
            list_1.append(str(ptr_1.val))
            ptr_1 = ptr_1.next
        while ptr_2:
            list_2.append(str(ptr_2.val))
            ptr_2 = ptr_2.next
        print(list_1, " ", list_2)
        print(reversed(list_1), " ", reversed(list_2))
        st_1 = int("".join(reversed(list_1)))
        st_2 = int("".join(reversed(list_2)))
        print(st_1, " ", st_2)
        ans = str(st_1 + st_2)[::-1]
        ans = [int(a) for a in ans]
        for v in ans:
            n.next = ListNode(v)
            n = n.next
        return root.next


