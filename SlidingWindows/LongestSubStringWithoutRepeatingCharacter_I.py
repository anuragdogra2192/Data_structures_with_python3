"""
Given a string s, find the length of the longest substring 
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
Notice that the answer must be a substring, "pwke" is a subsequence 
and not a substring.

Explaination: https://www.enjoyalgorithms.com/blog/longest-substring-without-repeating-characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global_max = 0
        left = 0
        
        if len(s) == 0:
            return 0

        while(left < len(s)):
            visited = [False for _ in range(256)]
            right = left
            
            while(right < len(s) and visited[ord(s[right])] == False):
                global_max = max(global_max, right - left + 1)
                visited[ord(s[right])] = True
                right += 1
            
            left += 1
        
        return global_max

"""
Time Complexity is O(n^2)
Space Complexity is O(1)
"""