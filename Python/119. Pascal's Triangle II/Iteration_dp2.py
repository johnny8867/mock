class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [1]
        
        while rowIndex > 0:
            for i in range(len(rows)-1, 0, -1):
                rows[i] = rows[i-1] + rows[i]
                
                
            rows.append(1)
            rowIndex -= 1
            
        return rows
    
    #O(k^2), O(k)