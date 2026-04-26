class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap: Dict[str, int] = {}
        for c in s:
            charMap[c] = charMap.get(c, 0) + 1
        

        for c in t:
            if c in charMap and charMap.get(c) != 0:
                charMap[c] = charMap.get(c) - 1
            else :
                return False
        
        for c in charMap:
            if charMap.get(c) != 0:
                return False
        
        return True