from collections import defaultdict
class Solution:
    def ThreeSum(self,nums:list[int])->list[list[int]]:
        nums.sort()
        count=defaultdict(int)
        for num in nums:
            count[num]+=1

        res=[]

        for i in range(len(nums)):
            count[nums[i]]-=1
            if i and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                count[nums[j]]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    continue

                target=-(nums[i]+nums[j])

                if count[target]>0:
                    res.append([nums[i],nums[j],target])

               

            for j in range(i+1,len(nums)):
                count[nums[j]]+=1

        return res

solution=Solution()
nums=[-1,0,1,2,-1,4]
print(solution.ThreeSum(nums))