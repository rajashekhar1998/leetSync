class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_vowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1

        left = 1
        right = k
        current_vowels = max_vowels

        for i in range(len(s)-k):
            if s[left-1] in vowels:
                current_vowels -= 1
            if s[right] in vowels:
                current_vowels += 1
            max_vowels = max(current_vowels,max_vowels)
            left += 1
            right += 1

        return max_vowels
        