class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Do try it the way they are saying
        """
        #nums.sort()

        # bubble sort
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                #swap
                    nums[j],nums[j+1] = nums[j+1],nums[j]
