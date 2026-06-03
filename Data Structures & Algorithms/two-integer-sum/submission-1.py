class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for i,n in enumerate(nums):
            if (target-n) in hash1:
                return[hash1[target-n],i]
            hash1[n] = i


            
        