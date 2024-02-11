"""
You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.

 

Example 1:

Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.
Example 2:

Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.
Example 3:

Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
 

Constraints:

1 <= n <= 109
"""
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)] 
        signed_sum = 0
        
        for i, digit in enumerate(digits):
            sign = 1 if i == 0 else (-1) ** (i % 2)
            signed_sum += sign * digit
        
        return signed_sum
            
