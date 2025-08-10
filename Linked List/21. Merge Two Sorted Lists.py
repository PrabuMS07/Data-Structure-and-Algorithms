"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode() # type: ignore
        t = dummy
        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val < head2.val:
                t.next = head1
                head1 = head1.next
            else:
                t.next = head2
                head2 = head2.next 
            t = t.next
        
        if head1:
            t.next = head1
            head1 = head1.next
        if head2:
            t.next = head2
            head2 = head2.next

        return dummy.next



        
        