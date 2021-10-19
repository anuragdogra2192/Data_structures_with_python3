def lengthofLongestSubstring(s):
    if not s:
        return 0

    start_index = 0
    last_index = 1
    subStrLength = 1
    while start_index < last_index and last_index < len(s):
        if (s[last_index] in s[start_index:last_index]):
            start_index += 1
            last_index = start_index + 1
        else:
            last_index += 1

        temp = last_index - start_index
        if(subStrLength<temp):
            subStrLength = temp
    return subStrLength
            
        
print(lengthofLongestSubstring("aabcabcbb"))
print(lengthofLongestSubstring("bbbbb"))
print(lengthofLongestSubstring("pwwkew"))
print(lengthofLongestSubstring("pw"))
print(lengthofLongestSubstring("pwk"))

#leetCode
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start_index = 0
        last_index = 1
        subStrLength = 1
        while start_index < last_index and last_index < len(s):
            if (s[last_index] in s[start_index:last_index]):
                start_index += 1
                last_index = start_index + 1
            else:
                last_index += 1

            temp = last_index - start_index
            if(subStrLength<temp):
                subStrLength = temp
        return subStrLength
'''