from typing import List

class solution:
    def containsDuplicate(self, nums: List[int]) ->bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
solution = solution()
test_case1 = [1,2,3,4]
test_case2 = [1,2,3,1]
print("Solution 1 is :", solution.containsDuplicate(test_case1))
print("Solution 2 is :", solution.containsDuplicate(test_case2))