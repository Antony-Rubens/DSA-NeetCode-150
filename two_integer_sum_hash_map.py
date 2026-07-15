from collections import defaultdict
class Solution:
    def twoSum(self,numbers:list[int],target:int)->list[int]:
        mp=defaultdict(int)
        for i in range(len(numbers)):
            tmp=target-numbers[i]

            if mp[tmp]:
                return[mp[tmp],i+1]
            mp[numbers[i]]=i+1
            
        return []
    
solution=Solution()
numbers=[1,2,3,4,5,6]
target=3
print(solution.twoSum(numbers,target))