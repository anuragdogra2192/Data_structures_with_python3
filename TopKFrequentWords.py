'''
nlog(k)  --> as heap used
'''
import heapq
def topkFrequent(words, k):
    #error checking
    if not words or k <= 0:
        return []
    
    #create dictionary
    wordsDict = {}
    for word in words:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    
    #print(wordsDict.items())

    #create heap
    # list of tuples
    #Heap in python(min heap) places the max value in the bottom and we need to have th max on top, therfore we do freq to -freq (5 tp -5) 
    #heap = [(freq, word) for word, freq in wordsDict.items()]
    heap = [(-freq, word) for word, freq in wordsDict.items()]
    print(heap)
    heapq.heapify(heap) #it does in-place
    # here the heapify will first sort with frequency and then by word 
    #return top k results from heap
    #total_result = [heapq.heappop(heap) for _ in range(k)] # we only need [1] i.e. words not [0] i.e. frequencies
    # so we add [1]
    #total_result = [heapq.heappop(heap)[1] for _ in range(k)] # we only need [1] i.e. words not [0] i.e. frequencies
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    print(result)

topkFrequent(["i", "love", "coding", "i", "love", "love", "leetcode", "baseball","baseball"], 2)