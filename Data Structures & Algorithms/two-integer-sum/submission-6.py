class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n,i in enumerate(nums):
            need = target - i
            if need in seen:
                return [seen[need], n]
            seen[i] = n
        