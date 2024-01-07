"""
Given a string s, return the longest
palindromic
substring
in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.


    """
from typing import Self
class Solution:
    def longestPalindrome(self,s:str) -> str:
     
        st=""
        s=s[1:len(s)-1]
        #print(s)
        StoreP=[]
        t=s[::-1]
        for i in range(len(s)):
            if s[i]==t[i]:
                st+=s[i]
                StoreP.append(i)
        if len(st)>1:
            for r in StoreP:
                
                print(r)
                
                
                
        
            
        return st
    
        
        
    
    
    if __name__=='__main__':
        #s="babad"
        #s = "cbbd"
        s="rotator"
        #print(s[::-1])
        #print(s[::])
        
        print(longestPalindrome(Self,s))