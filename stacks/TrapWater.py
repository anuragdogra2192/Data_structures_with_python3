"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented 
by array [0,1,0,2,1,0,1,3,2,1,2,1]. 

In this case, 6 units of rain water (blue section) are being trapped.
"""
"""
Time Complexity is O(n) and Space is O(n)
//https://www.youtube.com/watch?v=EdR3V5DBgyo&ab_channel=AlgorithmsMadeEasy
poppedElement = Stack.pop()
dist = rightIdx - leftIdx - 1
Formula used: Water_at_poppedUpElement = dist*(min(height[stack[-1]], height[i]) - poppedElement.height
"""

import collections
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        heightNIdx = collections.namedtuple('heightNIdx',
                                           ('id', 'height'))
        stack: List[heightNIdx] = []
        
        curr, water = 0, 0
        
        while curr<len(height):
            while(stack and height[curr]>stack[-1].height):
                top = stack.pop()
                if not stack:
                    break
                dist = curr - stack[-1].id - 1
                fill = dist * (min(height[curr], stack[-1].height)- top.height)
                    
                water+=fill
                
                    
            stack.append(heightNIdx(curr, height[curr]))
            curr+=1
        
        return water