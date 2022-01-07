'''
1568 / 1568 test cases passed.
Runtime: 111 ms
Memory Usage: 13.5 MB
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
    number1 = str(l1.val)
    number2 = str(l2.val)
    next1 = True
    next2 = True

    while next1 or next2:
        if next1:
            try:
                l1 = l1.next
                number1 += str(l1.val)                
            except: 
                next1 = False
        if next2:
            try:
                l2 = l2.next
                number2 += str(l2.val)                
            except: 
                next2 = False
        
    res = str(int(number1[::-1]) + int(number2[::-1]))
    result = ListNode(int(res[0]))
    
    if len(res)>1:
        for i in res[1::]:
            result = ListNode(int(i), result)

    return(result)
        
def main():
    
    #TestCase
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
