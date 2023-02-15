# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array 
# if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count_of_zeros = 0
        global_max = 0
        
        while right < len(nums):
            
            #Expand the window
            """
            Expand our window until we meet that condition 
            but before expanding the window, process the 
            element at the ‘right’ index.
            """
            if nums[right] == 0:
                count_of_zeros +=1
                        
            #Meet the condition to stop expansion        
            #Define condition to stop expanding our window
            
            while count_of_zeros > k:
                
            #Process the current window
                """
                If we meet our condition to stop expanding, 
                PROCESS the current window.
                """
                global_max = max(global_max, right-left)
                
                """
                Contract our current window, 
                but before contracting, 
                process the element at the ‘left’ index
                """
                if nums[left] == 0:
                    count_of_zeros -= 1
                left += 1
            right += 1
        
        if count_of_zeros <= k:
            global_max = max(global_max, right-left)
        
        return global_max