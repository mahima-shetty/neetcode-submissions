import random 
class Solution:
    def quicksort(self, nums: List[int], left: int, right: int) -> None:
        
        if left >= right:
            return


        r = random.randint(left, right)
        nums[r], nums[right] = nums[right], nums[r]

        pivot = nums[right]
        i = left
        for j in range(left, right):

            if nums[j] < pivot:
                nums[i], nums[j] = nums[j] , nums[i]
                i+=1

        nums[i] , nums[right] = nums[right] , nums[i]

        self.quicksort(nums,left, i-1)
        self.quicksort(nums, i+1, right)
        


    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums


