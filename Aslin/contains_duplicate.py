from typing import List
class Solution:
    def containsDuplicate(self, nums):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

solution=Solution()
testcase1=[1,3,2,1]
testcase2=[1,2,3,4]
print(solution.containsDuplicate(testcase1))
print(solution.containsDuplicate(testcase2))