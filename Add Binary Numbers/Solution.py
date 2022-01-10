'''
294 / 294 test cases passed.
Status: Accepted
Runtime: 28 ms, faster than 93.01% of Python3 online submissions for Add Binary.
Memory Usage: 14.1 MB, less than 93.79% of Python3 online submissions for Add Binary.
'''
class Solution(object):
    
    def add_one_by_one(self, x, y, carry_over):
        calc = x % 10 + y % 10 + carry_over
        return calc % 2, calc // 2 
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a[0] == '0': 
            return b
        elif b[0] == '0':
            return a
        
        a, b, carry_over, result = int(a), int(b), 0, ""
        
        while a and b:
            shifted_number, carry_over = self.add_one_by_one(a, b, carry_over)
            result += str(shifted_number)
            a, b = a // 10, b // 10
            
        if carry_over == 0 :
            if a :  return str(a) + result[::-1]
            if b :  return str(b) + result[::-1]
            
        while a:
            shifted_number, carry_over = self.add_one_by_one(a, 0, carry_over)
            result += str(shifted_number)
            a = a // 10
                        
        while b:
            shifted_number, carry_over = self.add_one_by_one(0, b, carry_over)
            result += str(shifted_number)
            b = b // 10
        
        if carry_over: 
            result += str(carry_over) 
        
        return(result[::-1])
            
            
