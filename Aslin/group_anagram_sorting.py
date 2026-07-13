from collections import defaultdict
class Solution:
    def groupAnagram(self,strs:list[str])->list[list[str]]:

        res=defaultdict(list)

        for s in strs:
            sortedS=''.join(sorted(s))
            res[sortedS].append(s)

        return list(res.values())
    
solution=Solution()
strs=["cat","eat","bat","tea","ate","rat","tar","tab"]
print(solution.groupAnagram(strs))