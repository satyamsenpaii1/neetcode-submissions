class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num=0
        age=0
        word=""
        for ele in details:
            for i in range(11,13):
                word = word+str(ele[i])
            age=int(word)
            if age>60:
                num+=1
                word=""
                age=0
            else:
                word=""
                age=0
        return num