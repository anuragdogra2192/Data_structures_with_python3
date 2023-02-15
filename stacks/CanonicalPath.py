"""
Other names:
Simplify Path
Normalize Pathnames
GetCanonicalPath
Shortest Equivalent File Path

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            raise ValueError("Empty path is not a valid format")
        
        path_names = [] # Uses list as stack
        
        
        #if path[0] == '/':
        #    path_names.append('/')
        
        for token in path.split('/'):
            if token in ['.','']:
                continue
            
            if token =='..':
                if not path_names or path_names[-1]=='..':
                    path_names.append(token)
                else:
                    path_names.pop()
            
            else:
                if(token!='/'):
                    path_names.append(token)
        
        if  not path_names:
            return  '/'
        result =  ""
        while path_names:
            temp = path_names.pop()
            if temp != "/" and temp !="" and temp!="..":
                result = "/"+temp+result
        
                
        if not result:
            return '/'
        
        return result

"""
Time Complexity is O(n) and 
"""