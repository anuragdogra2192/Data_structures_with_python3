
import heapq

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

