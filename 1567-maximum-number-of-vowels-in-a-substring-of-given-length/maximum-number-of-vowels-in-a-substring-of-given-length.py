class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_vowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1

        current_vowels = max_vowels

        for i in range(k, len(s)):
            if s[i-k] in vowels: current_vowels -= 1
            if s[i] in vowels: current_vowels += 1
            max_vowels = max(current_vowels,max_vowels)
            if max_vowels == k: return k

        return max_vowels
        