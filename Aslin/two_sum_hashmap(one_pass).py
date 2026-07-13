class Solution:
    def twoSum(self,nums:list[int],target:int)->list[int]:

        prevMap={}

        for i, n in enumerate(nums):

            diff = target-n

            if diff in prevMap:

                return[prevMap[diff], i]
            
            prevMap[n]=i

solution=Solution()
nums=[3,4,5,6,7]
target=7
print(solution.twoSum(nums,target))