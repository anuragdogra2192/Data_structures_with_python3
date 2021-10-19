##Wrong because sum of chars can be same for diff words with diff chars
#For example: duh, ill
def groupAnagrams(L):
    anagrams = {}
    for s in L:
        sum = 0
        for c in s: 
            sum += ord(c) 
        
        if sum in anagrams:
            anagrams[sum].append(s)
        else:
            tempList = []
            tempList.append(s)
            anagrams[sum] = tempList
    
    #print(anagrams)
    Output = []
    for key in anagrams:
        Output.append(anagrams[key])
    
    print(Output)
strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

