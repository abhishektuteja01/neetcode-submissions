class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        post = [1]*n
        res = [1]*n
        Pre = 1
        for i in range(0,len(nums)):
            pre[i] *= Pre
            Pre *= nums[i]
        Post = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] *= Post
            Post *= nums[i]
        for i in range(len(nums)):
            res[i] = pre[i] * post [i] 
        return res

        