class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''
        for c in s:
            if c.isalnum():
                newStr+= c.lower()
        return newStr == newStr[::-1]
solution = Solution()
testcase = "Was it a car or a cat I saw?"
print(solution.isPalindrome(testcase))