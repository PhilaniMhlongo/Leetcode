"""
Given a string s, find the length of the longest
substring
without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_pointer = 0
        b_pointer = 0
        max_length = 0

        hash_set = set()
        while b_pointer < len(s):
            if s[b_pointer] not in hash_set:
                hash_set.add(s[b_pointer])
                b_pointer += 1
                max_length = max(len(hash_set), max_length)
            else:
                hash_set.remove(s[a_pointer])
                a_pointer += 1

        return max_length

