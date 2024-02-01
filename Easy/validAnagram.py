"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        char_count_s = {}
        char_count_t = {}

        
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        
        return char_count_s == char_count_t
            
