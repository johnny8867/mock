class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        contain = {}
        
        for item in strs:
            if ''.join(sorted(item)) not in contain:
                contain[''.join(sorted(item))] = [item]
            else:
                contain[''.join(sorted(item))].append(item)
            
            
        return contain.values()
        
        #for key, value in contain.items():
        
        #(nlogn * n)
        
        #(n*k) where k is the length of strs
        
        #nlogn for sort....
            