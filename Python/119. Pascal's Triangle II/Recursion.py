class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevRow = self.getRow(rowIndex - 1)
        
        curRow = [1]
        
        for i in range(len(prevRow)-1, 0, -1):

            curRow.append(prevRow[i] + prevRow[i-1])
            
        curRow.append(1)
        
        return curRow
    
    #O(n^2), #O(n)