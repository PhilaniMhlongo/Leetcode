"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].



"""
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output_arr = deque()
        if not digits:
            return list(output_arr)

        output_arr.append("")

        char_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        for i in range(len(digits)):
            index = int(digits[i])
            while len(output_arr[0]) == i:
                permutation = output_arr.popleft()
                for c in char_map[index]:
                    output_arr.append(permutation + c)

        return list(output_arr)


