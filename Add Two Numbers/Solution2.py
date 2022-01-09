'''
Runtime: 52 ms, faster than 94.83% of Python online submissions for Add Two Numbers.
Memory Usage: 13.4 MB, less than 91.96% of Python online submissions for Add Two Numbers.
'''
class Solution(object):
   
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(val = (l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10
        current_node = result
        
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next
            
        while l1.next:
            l1 = l1.next
            current_node.next = ListNode(val = (carry_over + l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10
            current_node = current_node.next
        while l2.next:
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10
            current_node = current_node.next
            
        if carry_over > 0:
            current_node.next = ListNode(val = 1)
        
        return result
            
