class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = dict()
        for num in nums:
            if num in nums2 : 
                return True
            nums2[num] = 1
        
        return False