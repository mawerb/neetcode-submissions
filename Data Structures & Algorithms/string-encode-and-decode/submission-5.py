class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""

        sizes, encoded = [], ""
        
        for s in strs:
            size = len(s)
            sizes.append(size)
            encoded += (str(size))
            encoded += (',')
        encoded += "#"
        for s in strs:
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        size,decoded,i = [],[],0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            size.append(int(curr))
            i += 1
        i += 1
        for sz in size:
            decoded.append(s[i:i + sz])
            i += sz
        return decoded


