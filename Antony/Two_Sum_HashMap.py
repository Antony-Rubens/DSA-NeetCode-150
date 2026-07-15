from typing import List
class Solution:
    def two_sum(self, numbers: List[int], target: int ) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []
    
solution = Solution()
testcase = "Was it a car or a cat I saw?"
print(solution.ValidPalindrome(testcase))