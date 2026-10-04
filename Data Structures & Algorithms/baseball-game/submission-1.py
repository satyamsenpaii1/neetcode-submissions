class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        ## given in the question that there will always be records present in the
        ## stack before any operation + , c or d so no need to worry about emptyness

        for i in range(len(operations)):
            if operations[i] != '+' and operations[i] != 'C' and operations[i] !='D':
                records.append(int(operations[i]))
            
            elif operations[i] == '+':
                records.append(records[-1] + records[-2])
            
            elif operations[i] == 'C':
                records.pop()
            
            elif operations[i] == 'D':
                records.append(records[-1]*2)
        
        return sum(records)