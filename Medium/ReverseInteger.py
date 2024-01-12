"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1


"""

class Solution:
    def reverse(self, x: int) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

    
        sign = 1 if x >= 0 else -1
        x = abs(x)

        reversed_num = 0

        while x > 0:
            digit = x % 10
            
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        return sign * reversed_num

