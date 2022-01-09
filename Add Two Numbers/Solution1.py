'''
1568 / 1568 test cases passed.
Status: Accepted
Runtime: 89 ms
Memory Usage: 13.4 MB
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    number1 = "" 
    number2 = ""
    
    while l1 or l2:
        if l1:
            number1 += str(l1.val)
            l1 = l1.next
        if l2:
            number2 += str(l2.val)
            l2 = l2.next    
    res = str(int(number1[::-1]) + int(number2[::-1]))
    result = ListNode(int(res[0]))
    if len(res)>1:
        for i in res[1::]:
            result = ListNode(int(i), result)

    return result

def main():
    
    List1 = ListNode(2,ListNode(4,ListNode(3))) # (2 -> 4 -> 3)
    List2 = ListNode(5,ListNode(6,ListNode(4))) # (5 -> 6 -> 4)
    L1, L2 = List1, List2
    res = addTwoNumbers(L1, L2)
    nodes = []
    while res:
        nodes.append(str(res.val))
        res = res.next
    
    print(f"Result = ({'->'.join(nodes)})")

if __name__ == '__main__':
    main()
