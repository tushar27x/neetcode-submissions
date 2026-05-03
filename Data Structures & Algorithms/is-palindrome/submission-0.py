class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp: str = re.sub(r'[^a-z0-9]', '', s.lower())
        n = len(temp)
        l,r = 0, n-1

        while l<r:
            if temp[l] != temp[r]:
                return False

            l += 1
            r -= 1

        return True    