class Solution:
    def twoSum(self,numbers:list[int],target:int)->list[int]:
        l,r=0,len(numbers)-1

        while l<r:
            curNum=numbers[l]+numbers[r]

            if curNum>target:
                r-=1

            elif curNum<target:
                l+=1

            else:
                return[l+1,r+1]
            
        return []
    
solution=Solution()
numbers=[1,2,3,4,5,6S]
target=3
print(solution.twoSum(numbers,target))