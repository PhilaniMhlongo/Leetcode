"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output_arr = []

        fizz, buzz = 0, 0
        for i in range(1, n + 1):
            fizz += 1
            buzz += 1

            if fizz == 3 and buzz == 5:
                fizz = 0
                buzz = 0
                output_arr.append("FizzBuzz")
            elif fizz == 3:
                fizz = 0
                output_arr.append("Fizz")
            elif buzz == 5:
                buzz = 0
                output_arr.append("Buzz")
            else:
                output_arr.append(str(i))

        return output_arr
        

