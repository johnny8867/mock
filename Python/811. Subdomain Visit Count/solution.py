class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def store_key(lookup, string, value):
            if string not in lookup:
                lookup[string] = value
            else:
                lookup[string] += value

        contain = {}

        for item in cpdomains:
            temp_store = item.split()
            count = int(temp_store[0])
            store_key(contain, temp_store[1], count)
            
            index = 0
            while index < len(temp_store[1]):
                if temp_store[1][index] == '.':
                    store_key(contain, temp_store[1][index+1:], count)
                index += 1

        result = []

        for key, value in contain.items():
            result.append(str(value) +' ' +key)

        return result
        #Time: O(N), Space: O(N)
                    
        