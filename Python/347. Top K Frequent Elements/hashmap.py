class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        contain = {}
        for item in nums:
            contain[item] = contain.get(item, 0) + 1
        
        contain = sorted(contain.items(), key = lambda item: item[1], reverse = True)
        
        
        result = []
        
        for key, value in contain:
            if k > 0:
                result.append(key)
                k -= 1
            elif k == 0:
                break
                
        return result
    
    #(O(nlogn)+ n + k)
    #(n+k)