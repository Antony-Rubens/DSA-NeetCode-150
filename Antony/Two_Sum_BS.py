from typing import List
class Solution:
    def twosum(self, numbers: List[int], target: int)-> List[int]:
        for i in range(len(numbers)):
            l , r =  i+1 , len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = (l+r)//2
                if numbers[mid]== tmp:
                    return[i+1, mid+1]
                elif numbers[mid]<tmp:
                    l=mid+1
                else:
                    r=mid-1
        return []
solution = Solution()
testcase = [2, 3, 4, 7]
target = 7
print(solution.twosum(testcase, target))