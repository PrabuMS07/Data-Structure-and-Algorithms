"""You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        cur = s.next
        s.next = None
        pre = None

        while cur:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem


        while pre:
            f,s = head.next,pre.next
            head.next = pre
            pre.next = f
            pre = s
            head = f



