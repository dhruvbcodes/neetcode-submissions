# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        st = []
        
        while curr != None:
            st.append(curr)
            curr = curr.next
        
        curr = head
        n = len(st)//2
        for _ in range(n):
            temp = curr.next
            curr.next = st.pop()
            curr.next.next = temp
            curr = temp

        curr.next = None
        