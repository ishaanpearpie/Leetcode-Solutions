import math
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        l = []
        for j in range(numRows):
            l = []
            for i in range(j+1):
                l.append(math.comb(j,i))
            ans.append(l)
        return ans