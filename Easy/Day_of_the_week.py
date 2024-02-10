"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

 

Constraints:

    The given dates are valid dates between the years 1971 and 2100.



"""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
        if month < 3:
            month += 12
            year -= 1
        
        q = day
        m = month
        K = year % 100
        J = year // 100
        
        h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
        
        return days_of_week[(h + 6) % 7] 
        
