class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# input l1 = [2, 4, 3], l1 = [5, 6, 4]
# output [7, 0, 8]
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_tail = result
        carry = 0

        l1 = ListNode(0)
        l2 = ListNode(0)

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

if __name__ == '__main__':
    a = Solution()
    a.addTwoNumbers(l1=[2,5,3], l2=[5,6,4])