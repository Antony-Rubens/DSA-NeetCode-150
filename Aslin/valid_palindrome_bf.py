class Solution:
    def isvalidPalindrome(self,s:str)->bool:
        newStr=''

        for c in s:
          if c.isalnum():
             newStr+=c.lower()

        return newStr==newStr[::-1]
    
solution=Solution()
s='was it a car or a cat i saw'
print(solution.isvalidPalindrome(s))