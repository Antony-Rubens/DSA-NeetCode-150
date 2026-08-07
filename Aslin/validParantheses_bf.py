class Solution:
    def ValidParantheses(self,s:str)->bool:
        while '()' in s or '{}' in s or '[]' in s :
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')

        return s==''

solution=Solution()
s='({[]})'
print(solution.ValidParantheses(s))