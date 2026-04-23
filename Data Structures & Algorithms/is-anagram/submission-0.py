class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elements = {}
        for char in s:
            if char in elements:
                elements[char] += 1
            else:
                elements[char] = 1
        
        for char in t:
            if char in elements:
                elements[char] -= 1
                if elements[char] < 0:
                    return False
            else:
                return False

        return True
        