"""
Other names
Is A String Well Formed?
Balanced brackets
"""
#LeetCode
class Solution:
    def isValid(self, s: str) -> bool:
        left_chars = []
        lookup = {  '(':')',
                    '{':'}',
                    '[':']'
                 }
        for c in s:
            if c in lookup:
                left_chars.append(c)
            
            elif not left_chars or lookup[left_chars.pop()] != c:
                return False
        
        if left_chars: #Check if it contains an element
            return False
        
        return True

"""
Time complexity: O(n)
Space Complexity: O(1) 
"""
a, b = [], {'(':')'}
print(a)
print(b)

c = '('
if c in b:
    print("adada")

if a:
    print("Aadd")

d=')'
if not a or b['(']!=c:#Means a is empty list
    print("AAA")
print()

#hackerRank
def isBalanced(s):
    left_chars = []
    lookup = {  '(':')',
                '{':'}',
                '[':']'
            }
    for c in s:
        if c in lookup:
            left_chars.append(c)
            
        elif not left_chars or lookup[left_chars.pop()] != c:
            return "NO"
        
    if left_chars: #Check if it contains an element
        return "NO"
        
    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
