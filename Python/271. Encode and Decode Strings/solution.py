class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ''
        for word in strs:
            result += str(len(word)) + '#' + word

        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        start = 0
        while start < len(s):
            j = start
            while s[j] != '#':
                j += 1
            word_length = int(s[start:j])
            word = s[j+1: j + 1 + word_length]
            start = j + 1 + word_length
            result.append(word)
        return result
        #O(N), O(N)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))