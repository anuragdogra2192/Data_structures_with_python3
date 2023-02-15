# MAX CONSECUTIVE ONES II 
# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
# Input: [1,0,1,1,0]
# Output: 4

def sliding_window(nums):
    left, right = 0, 0        # Our window bounds
    count_of_zeroes = 0       # Track how many 0’s are in the window
    global_max = 0            # Track the maximum, overall
    # Iterate over elements in our input
    while right < len(nums):
        # Expand the window 
        if nums[right] == 0:        
            count_of_zeroes += 1
        # Meet the condition to stop expansion
        while count_of_zeroes == 2:
        # Process the current window
            global_max = max(global_max, right - left)
        # Contract the window
            if nums[left] == 0:
                count_of_zeroes -= 1
            left += 1
        right += 1
    if count_of_zeroes < 2:
        global_max = max(global_max, right-left)
    return global_max