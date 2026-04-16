# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        count=0
        while curr is not None:
            print(curr.val)
            count+=1
            curr= curr.next
        
        temp = head

        for i  in range(0,count // 2):

            temp = temp.next
        return temp
        