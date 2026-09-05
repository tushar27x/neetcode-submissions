class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = Counter(words[0])
        for w in words:
            chars &= Counter(w)
        
        return list(chars.elements())
