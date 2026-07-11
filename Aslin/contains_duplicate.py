class Solution:
    def isContainsDuplicate(self,nums:list[int])->bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
solution=Solution()
nums1=[1,2,3,3]
nums2=[1,2,3,4]
print(solution.isContainsDuplicate(nums1))
print(solution.isContainsDuplicate(nums2))