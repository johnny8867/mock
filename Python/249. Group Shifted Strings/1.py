#Need to make key the differences of evach adjcent character
#Since you can not use a mutable type as key, we need to keep differences in tuple or make it str.

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        contain = {} #key will be the differences b/w each adjancent characters
        
        for item in strings:
            key = []
            for i in range(len(item)-1):
                difference = (ord(item[i+1]) - ord(item[i])) + 26

                key.append(str(difference % 26))
            key = ','.join(key)
            contain[key] = contain.get(key,[]) + [item]
            
        return contain.values()
    
    #O(N *K)  NN be the length of strings and KK be the maximum length of a string in strings.
    #O(N*K)