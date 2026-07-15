from typing import List
class Solution:
    def Two_sum(self, numbers: List[int], target: int)-> List[int]:
        l , r = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l]+ numbers[r]
            if curSum< target:
                l+=1
            if curSum> target:
                r-=1
            else:
                return [l+1,r+1]
        return []
solution = Solution()
testcase = [2, 3, 4, 7]
target = 7
print(solution.twosum(testcase, target))