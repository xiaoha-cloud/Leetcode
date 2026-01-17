from typing import List
from collections import defaultdict

MOD = 10**9+7
class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        px =0
        sum_dp1 = defaultdict(int)
        sum_dp2 = defaultdict(int)

        dp1=dp2=0

        for v in nums:
            px ^=v
            dp1=sum_dp2[px^ target1] %MOD
            if px == target1:
                dp1 = (dp1+1)%MOD

            dp2 = sum_dp1[px ^ target2]%MOD

            sum_dp1[px]=(sum_dp1[px]+dp1)%MOD
            sum_dp2[px]=(sum_dp2[px]+dp2)%MOD

        return (dp1+dp2)%MOD