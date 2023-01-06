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
            
            new_array = temp_store[1].split('.')
            
            for i in range(len(new_array)):
                store_key(contain, '.'.join(new_array[i:]), count)

        result = []

        for key, value in contain.items():
            result.append(str(value) +' ' +key)

        return result
        #Time: O(N), Space: O(N)
                    
        