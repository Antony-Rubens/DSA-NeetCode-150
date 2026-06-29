class Solution:
    def twoSum(self,nums: list[int],target:int)-> list[int]:
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            
            prevMap[n]=i

solution=Solution()
case=[1,2,3,4]
target=5
print (solution.twoSum(case,target))