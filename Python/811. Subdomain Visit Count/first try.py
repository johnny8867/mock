class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        contain = {}

        for item in cpdomains:
            temp_store = item.split()
            count = int(temp_store[0])
            
            if temp_store[1] not in contain:
                contain[temp_store[1]] = count
            else:
                contain[temp_store[1]] += count
            
            for i in range(len(temp_store[1])):
                if temp_store[1][i] == '.':
                    if temp_store[1][i+1:] not in contain:
                        contain[temp_store[1][i+1:]] = count
                    else:
                        contain[temp_store[1][i+1:]] += count

        result = []

        for key, value in contain.items():
            result.append(str(value) +' ' +key)

        return result
        #Time: O(N), Space: O(N)
                    
        