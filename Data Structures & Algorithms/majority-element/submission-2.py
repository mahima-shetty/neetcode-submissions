class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len( nums)
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        for i,k in hashmap.items():
            if k > n//2:
                return i