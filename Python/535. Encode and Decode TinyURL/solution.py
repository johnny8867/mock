class Codec:
    def __init__(self):

        self.encode_map = {}
        self.decode_map = {}
        self.base = "https://tinyurl.com/"
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        to_put = self.base + str(len(self.encode_map))
        
        if longUrl not in self.encode_map:
            self.encode_map[longUrl] = self.base + str(len(self.encode_map))
            self.decode_map[to_put] = longUrl

        return to_put

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]
    #O(1), O(1)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))