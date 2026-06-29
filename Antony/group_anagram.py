from typing import List
from collections import defaultdict
class solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())
solution = solution()
testcase = ["ant","tan","car","rac","tap","pat","apt"]
print(solution.groupAnagram(testcase))