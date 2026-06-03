class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set()
        for n in nums:
            if n in output:
                return True
            output.add(n)
        return False