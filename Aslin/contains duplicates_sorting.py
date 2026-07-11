class Solution:
    def isContainsDuplicates(self,nums:list[int])->bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
    
solution=Solution()
nums1=[1,2,3,3]
nums2=[1,2,3,4]
print(solution.isContainsDuplicates(nums1))
print(solution.isContainsDuplicates(nums2))