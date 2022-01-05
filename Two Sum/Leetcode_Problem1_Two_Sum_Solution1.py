class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        visited_indexes = []
        elements = []

        for i,v in enumerate(self.nums):
            if self.target-v in self.nums:
                j = self.nums.index(self.target-v)
                if i != j :
                    if j in visited_indexes and j<len(self.nums)-1:
                        try:
                            k = self.nums.index(self.target-v,j+1)
                            j = k
                        except:
                            pass
                    visited_indexes.append(j)
                    if i not in elements and j not in elements:        
                        elements.append(min(i,j))
                        elements.append(max(i,j))

        return elements

def main():
    test_case = Solution()
    L = [1,2,3,2,4,5,6,7]
    target = 4
    print(test_case.twoSum(L, target))

if __name__ == '__main__':
    main()
