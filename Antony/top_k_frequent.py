from typing import List
class solution:
    def topk(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
solution = solution()
test = [1,2,3,4,3,2,1,2,2]
k= 2
print(solution.topk(test,k))