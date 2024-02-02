"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.



"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Pad the shorter binary string with leading zeros
        a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))

        for i in range(len(a) - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])
        
