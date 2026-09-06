# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None

        merge_list = ListNode()
        merge_list_head = ListNode()
        merge_list.next = merge_list_head

        while list1 and list2:

            val1 = list1.val
            val2 = list2.val
            # print(val1, val2)

            if val1 > val2: 
                merge_list_head.val = val2
                list2 = list2.next
            else:
                merge_list_head.val = val1
                list1 = list1.next

            if list1 or list2:
                merge_list_head.next = ListNode()
                merge_list_head = merge_list_head.next
        
        while list1:

            val = list1.val
            merge_list_head.val = val

            list1 = list1.next
            if list1:
                merge_list_head.next = ListNode()
                merge_list_head = merge_list_head.next
        
        while list2:

            val = list2.val
            merge_list_head.val = val

            list2 = list2.next
            if list2:
                merge_list_head.next = ListNode()
                merge_list_head = merge_list_head.next
        
        return merge_list.next
        
        
        



        