class Solution:
    def longestConsecutive(self,nums:list[int])->int:
        numSet=set(nums)
        longest=0

        for num in numSet:
            if (num-1) not in numSet:
                length=1

                while (num+length) in numSet:
                    length+=1
                longest=max(longest,length)
        return longest
    
solution=Solution()
numSet=[2,20,4,10,3,4,1]
print(solution.longestConsecutive(numSet))