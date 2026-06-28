class solution:
    def isAnagram(self, s: str , t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])- ord('a')] +=1
            count[ord(t[i])- ord('a')] -=1
        for val in count:
            if val != 0:
                return False
        return True

solution = solution()
test1 = "anagram"
test2 = "naaragm"
print("The answer is:", solution.isAnagram(test1,test2))