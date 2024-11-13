from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = 0
        for i in range(len(nums)):
            sum+= nums[i]
            if sum<0:
                sum = 0
            if sum>maxi:
                maxi = sum
        if maxi == 0:
            return max(nums)
        return maxi


        
        