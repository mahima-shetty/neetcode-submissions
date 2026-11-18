class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        array = []
        for num, cnt in count.items():
            array.append([cnt, num])
        array.sort()


        result = []
        while len(result) < k:
            result.append(array.pop()[1])

        return result