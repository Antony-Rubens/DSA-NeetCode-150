from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
solution = Solution()
testcase: list = [10,20,30,40]
print(solution.product_except_self(testcase))
