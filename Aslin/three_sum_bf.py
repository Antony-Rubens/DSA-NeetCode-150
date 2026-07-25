class Solution():
    def ThreeSum(self,nums:list[int])->list[list[int]]:
        res=set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp=[nums[i],nums[j],nums[k]]

                        res.add(tuple(temp))

        return [list(i) for i in res]

solution=Solution()
nums=[-1,0,1,2,-1,4]
print(solution.ThreeSum(nums))