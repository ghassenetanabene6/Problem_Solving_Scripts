import numpy as np

class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)
    def index(self, value, start=0):
        return np.where(self[start::] == value)[0][0]
    

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = myarray(nums)
        self.target = target
        visited_indexes = np.array([], dtype=int)
        elements = np.array([], dtype=int)

        for i,v in enumerate(self.nums):
            if self.target-v in self.nums:
                j = self.nums.index(self.target-v)
                
                if i != j :
                    if j in visited_indexes and j<len(self.nums):
                        try:
                            k = self.nums.index(self.target-v,j+1)
                            j = k
                        except:
                            pass
                    visited_indexes = np.append(visited_indexes,j)
                    if i not in elements and j not in elements:        
                        elements = np.append(elements, min(i,j))
                        elements = np.append(elements, max(i,j))
        return list(elements)

def main():
    test_case = Solution()
    L = [1,2,3,2,4,5,6,7]
    target = 4
    print(test_case.twoSum(L, target))

if __name__ == '__main__':
    main()
