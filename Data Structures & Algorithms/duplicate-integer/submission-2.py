class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = []
        for n in nums:
            if n in output:
                return True
            output.append(n)
        return False