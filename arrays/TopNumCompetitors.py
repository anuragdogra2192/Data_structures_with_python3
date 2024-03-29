
#import heapq
'''
Input
The input to the function/method consists of five arguments - numCompetitors, an integer representing the number of competitors for the Echo device;
topNCompetitors, is an integer representing the maximum number of competitors that Amazon wants to identify;
competitors, a list of strings representing the competitors;
numReviews, an integer representing the number of reviews from different websites that are identified by the automated webcrawler;
reviews, a list of string where each element is a string that consists of space-separated words representing user reviews.

Output
Return a list of strings representing Amazon's top N competitors in order of most frequently mentioned to least frequent.

Note
The comparison of strings is case-insensitive. If the value of topNCompetitors is more than the number of competitors discussed in the reviews
then output the names of only the competitors mention.
If competitors have the same count (e.g. newshop=2, shopnow=2, mymarket=4), sort alphabetically. topNCompetitors=2, Output=[mymarket, newshop]

Example
Input:
numCompetitors=6
topNCompetitors = 2
competitors = [newshop, shopnow, afashion, fashionbeats, mymarket, tcellular]
numReviews = 6
reviews = [
"newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"]

Output
["newshop", "fashionbeats"]

Explanation
"newshop" is occurring in 3 different reviews. "fashionbeats" is occuring in 2 different user reviews and "mymarket" is occurring in only 1 review.
'''
def TopNumCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    competitors.sort()
    competitorsDict = {}
    for c in competitors:
        for r in reviews:
            r = r.lower()
            if c in r:
                if c in competitorsDict:
                    competitorsDict[c] += 1
                else:
                    competitorsDict[c] = 1
    
    #print(competitorsDict)
    ReverseDict = {}
    for competitor, freq in competitorsDict.items():
        ReverseDict[freq] = competitor

    # heapq.heapify(heap)
    ReverseDict_items = ReverseDict.items()
    sorted_items = sorted(ReverseDict_items)
    output = []
    print(sorted_items)

    for i in range(topNCompetitors, 0, -1) :
         output.append(sorted_items[i][1])
    
    print(output)


numCompetitors = 6
topNCompetitors = 2
competitors = ["newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"]
numReviews = 6
reviews = ["newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"]

TopNumCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews)

