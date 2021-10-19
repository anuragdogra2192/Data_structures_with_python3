"""
A palindromic string is one which reads the same when it is reversed.
"""

def is_palindromic(s):
    #Note that s[~i] for i in [0, len(s) - 1] is s[-(i+1)]. For example i = 28, then ~i = -29.
    #return all(s[i] == s[~i] for i in range(len(s) // 2))
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False
    
    return True
    #One liner 
    #return all(s[i] == s[~i] for i in range(len(s) // 2))
s = input("Enter a string: ")

print("The given string is palindromc or not", is_palindromic(s))