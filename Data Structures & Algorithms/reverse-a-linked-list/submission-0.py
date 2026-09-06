# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        reverse_head = ListNode()
        reverse_head.next = ListNode()
        reverse_list = reverse_head.next
        vals = []

        while head:

            # reverse_list.val = head.val
            # reverse_list.next = ListNode()
            # reverse_list = reverse_list.next
            vals.append(head.val)
            head = head.next

        for i, val in enumerate(vals[::-1]):
            reverse_list.val = val
            if i != len(vals) -1:
                reverse_list.next = ListNode()
                reverse_list = reverse_list.next

        
        return reverse_head.next
        