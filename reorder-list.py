# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast.next and fast.next.next:
            print(fast.next.next.val)
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next
        revhead = None 
        slow.next = None
        while temp:
            newtemp = temp.next
            temp.next = revhead
            revhead = temp
            temp = newtemp
        
            
        current = head
        while revhead:
            newrevhead = revhead.next
            newcurrent = current.next
            current.next = revhead
            current.next.next = newcurrent
            current = newcurrent
            revhead = newrevhead

        
            
            
            
            
        