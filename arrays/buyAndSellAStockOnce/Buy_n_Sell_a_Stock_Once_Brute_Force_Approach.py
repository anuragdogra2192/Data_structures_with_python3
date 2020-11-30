#!/usr/bin/python3

#Buy n sell stock once to maximizing profit
# First buy then sell
#Brute-force algorithm

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# i is the buying index
# j is the selling index

def maximized_profit(A):
    maximized =  0;
    for i in range(0,len(A)):
        for j in range(i+1, len(A)):
            temp = A[j] - A[i]
            if temp >= maximized:
                maximized = temp
                Buy = A[i]
                Sell = A[j]
    print(" Maximized profit: ", maximized)
    return (Buy, Sell)

X = maximized_profit(A)
print("The buying and selling price: ", X[0], "and ", X[1])