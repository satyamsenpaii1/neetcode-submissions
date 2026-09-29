class Solution:
    def isValid(self, s: str) -> bool:
        ## let's try doing stack implementation
        if len(s)%2 != 0:
            return False
        lis = []
        for i in range(int(len(s))):
            if s[i] == "(" or s[i] == "{" or s[i] == "[" :
                lis.append(s[i])

            elif s[i] == ")" and lis and lis[-1] == "(" :
                lis.pop()
            
            elif s[i] == "}" and lis and lis[-1] == "{":
                lis.pop()
            
            elif s[i] == "]" and lis and lis[-1] == "[":
                lis.pop()
            else:
                return False
            
        return not lis
