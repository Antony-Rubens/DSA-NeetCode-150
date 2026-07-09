from typing import List

class solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []

solution = solution()
testcase = [2, 3, 4, 7]
target = 7
print(solution.twosum(testcase, target))