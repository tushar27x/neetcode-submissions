class Solution:
    def sort_string(self, s: str) -> str:
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs: Dict[str, List[str]]  = {}
        for s in strs:
            sorted_str = self.sort_string(s)
            grouped_strs[sorted_str]  = grouped_strs.get(sorted_str, []) + [s]


        return list(grouped_strs.values())
        