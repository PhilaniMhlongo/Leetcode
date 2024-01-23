class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

    # Reverse the integer
        reversed_x = 0
        original_x = x
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

    # Compare the reversed integer with the original one
        return original_x == reversed_x
        
