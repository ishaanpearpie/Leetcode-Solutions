from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            flag = True
            temp = nums2.index(i)
            for j in range(temp+1, len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    flag = False
                    break
            if flag:
                ans.append(-1)
        return ans

                

        