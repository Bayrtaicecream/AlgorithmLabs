class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        return self.divide_and_conquer(s)
    
    def divide_and_conquer(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        set_chars = set(s)
        for i, char in enumerate(s):
            if char.lower() not in set_chars or char.upper() not in set_chars:
                left = self.divide_and_conquer(s[:i])
                right = self.divide_and_conquer(s[i+1:])
                return left if len(left) >= len(right) else right
        return s