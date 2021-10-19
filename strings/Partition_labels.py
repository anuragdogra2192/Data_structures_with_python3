

from typing import Container


'''
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
'''

def partitionLabels(s):
    # error checks
    if not s:
        return []

    dict = {}
    for i in range(len(s)):
        dict[s[i]] = i

    #print(dict) 
    
    last, first = 0, 0
    result = []
    for i in range(len(s)):
        last = max(last, dict[s[i]])
        if i == last:
            result.append(last - first + 1)
            first = i + 1
    
    return result

s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
s = "eccbbbbdec"
print(partitionLabels(s))