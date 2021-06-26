# Input: head = [4,5,1,9], node=5
# Output: [4,1,9]

class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None 


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


l1 = ListNode(x=1)

l2 = ListNode(x=2)
l1.next = l2

l3 = ListNode(x=3)

s = Solution()
s.deleteNode(l1)

