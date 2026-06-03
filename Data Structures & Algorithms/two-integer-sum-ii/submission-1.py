class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i,n in enumerate(numbers):
            res[n] = i
            diff = target - n
            if (diff in res) and (res[diff] != i):
                return [res[diff]+ 1,res[n]+1] 
        