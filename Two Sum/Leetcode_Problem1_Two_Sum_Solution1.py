class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,v in enumerate(nums):
            if target-v in nums:
                j = nums.index(target-v)
                if i != j :
                    return [min(i,j),max(i,j)]
               
        return 
 
class SolutionForManyValidAnswers(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited_indexes = []
        elements = []

        for i,v in enumerate(nums):
            if target-v in nums:
                j = nums.index(target-v)
                if i != j :
                    if j in visited_indexes and j<len(nums)-1:
                        try:
                            k = nums.index(target-v,j+1)
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
