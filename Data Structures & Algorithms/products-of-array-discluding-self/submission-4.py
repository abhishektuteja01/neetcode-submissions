class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*(n)
        Pre = 1
        for i in range(0,n):
            res[i] *= Pre
            Pre *= nums[i]
        Post = 1
        for j in range(n-1,-1,-1):
            res[j] *= Post
            Post *= nums[j]
        return res

        