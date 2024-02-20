class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(s, reverse=False)
        second = sorted(t, reverse=False)
        if first == second:
            return True
        return False