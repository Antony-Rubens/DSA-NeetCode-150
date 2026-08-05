class Solution:
    def maxSlidingWindow(self, nums:list[int],k:int)->list[int]:
        output=[]
        for i in range(len(nums)-k+1):
            maxi=nums[i]
            for j in range(i,i+k):
                maxi=max(maxi,nums[j])

            output.append(maxi)

        return output

solution=Solution()
nums=[1,2,1,0,4,2,6]
k=3
print(solution.maxSlidingWindow(nums,k))