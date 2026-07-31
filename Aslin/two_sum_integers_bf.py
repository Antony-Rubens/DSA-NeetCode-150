class Solution:
    def TwoSumIntegers(self,numbers:list[int],target:int)->list[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                
        return []
    
solution=Solution()
numbers=[1,2,3,4,5,6]
target=3
print(solution.TwoSumIntegers(numbers,target))
