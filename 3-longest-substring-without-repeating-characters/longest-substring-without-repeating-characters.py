class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] not in string_set:
                length = right - left +1
                longest = max(longest, length)
                string_set.add(s[right])
            else:
                while s[right] in string_set:
                    string_set.remove(s[left])
                    left = left + 1
                string_set.add(s[right])

        return longest
        