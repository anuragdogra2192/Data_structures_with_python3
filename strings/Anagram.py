def groupAnagrams(L):
    anagrams = {}
    for s in L:
        temp = sorted(s)
        temp = "".join(temp)
        if temp in anagrams:
            anagrams[temp].append(s)
        else:
            anagrams[temp] = [s]
    
    print(list(anagrams.values()))

    # Output = []
    # for key in anagrams:
    #     #for sorted list
    #     #Output.append(sorted(anagrams[key]))
    #     Output.append((anagrams[key]))
    
    # print(Output)
strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

'''
Leet Code
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            temp = sorted(s)
            temp = "".join(temp)
            if temp in anagrams:
                anagrams[temp].append(s)
            else:
                tempList = []
                tempList.append(s)
                anagrams[temp] = tempList
        #print(anagrams)
        Output = []
        for key in anagrams:
            Output.append(anagrams[key])
        
        return Output
'''