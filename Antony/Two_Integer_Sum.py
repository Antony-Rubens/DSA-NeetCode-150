from typing import List
class Solution:
    def twosum(self, numbers: List[int], target: int)-> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+ numbers[j]== target:
                    return [i+1,j+1]
        return []
Solution = Solution()
testcase = [1, 2, 3, 4, 5]
print(Solution.twosum(testcase, 9))