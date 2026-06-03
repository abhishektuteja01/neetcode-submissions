class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dset = defaultdict(set)
        for i in range(len(nums)):
            if nums[i] in dset[1]: 
                return True
            dset[1].add(nums[i])
        return False


         