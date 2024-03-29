from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx, count, l, index, n = max(nums), 0, 0, 0, len(nums)
        while index < n:
            k -= nums[index]==mx
            index += 1
            while k == 0:
                k += nums[l]==mx
                l += 1
            count += l
        return count