class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums, outputnums = {},[]

        for n in nums:
            countnums[n] = 1 + countnums.get(n,0)
        sorted_dict = sorted(countnums.items(), key=lambda item: item[1], reverse = True)
            
        top_keys = [key for key, value in sorted_dict][:k]
        return top_keys

        
        