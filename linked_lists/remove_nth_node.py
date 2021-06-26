# Input: head = [1,2,3,4,5], n =2
# Output: [1,2,3,5]


# Two point solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next


# class Solution1(object):
#     def removeNthFromEnd(self, head, n):
#         right = head 
#         result = ListNode()
#         result.next = head 
#         left = result 
#         l = 1
#         while right.next != None:
#             if l < n:
#                 right = right.next 
#             else:
#                 right = right.next 
#                 left = left.next 
#             l = l + 1

#         left.next = left.next.next 
#         return result.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        print(head)
        print(n)

        dummyTHICC = ListNode()
        dummyTHICC.next = head
        first = dummyTHICC
        second = dummyTHICC
        # Advances first pointer so that the gap between first and second is n ndoes apart
        i = 1
        while i <= n + 1:
            first = first.next 
            i += 1

        # Move first to the end, maintaining the gap
        while first != None:
            first = first.next 
            second = second.next

        second.next = second.next.next 
        return dummyTHICC.next


if __name__ == '__main__':
    l1 = ListNode(val=1)
    l2 = ListNode(val=2)
    l1.next = l2
    l3 = ListNode(val=3)
    l2.next = l3 
    l4 = ListNode(val=4)
    l3.next = l4 
    l5 = ListNode(val=5)
    l4.next = l5

    s = Solution()
    s.removeNthFromEnd(head=l1, n=2)
    # print(s.removeNthFromEnd(head=[1,2,3,4,5], n=2))