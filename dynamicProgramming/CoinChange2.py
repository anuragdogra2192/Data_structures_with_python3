"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

USING BOTTOMUP APPROACH
"""
# Wallet[0] = [[]]

# for l in Wallet[0]:
#     if 1 not in Wallet:
#         Wallet[1] = []
#     print(l)
#     temp = list(l)
#     temp.append(1)
#     Wallet[1].append(temp)
# print(Wallet)

# for l in Wallet[1]:
#     if 2 not in Wallet:
#         Wallet[2] = []
#     print(l)
#     temp = list(l)
#     temp.append(1)
#     Wallet[2].append(temp)
# print(Wallet)

# for l in Wallet[0]:
#     if 2 not in Wallet:
#         Wallet[2] = []
#     print(l)
#     temp = list(l)
#     temp.append(2)
#     Wallet[2].append(temp)
# print(Wallet)

'''
This below solution takes lots of time
'''
def makeCoinChanges(amount, coins):
    #Only use to find minimum number of coins 1)comment the Wallet 2)Uncomment the M[] related code 3)return M[amount]
    #M = [amount+1]*(amount+1)
    #M[0] = 0

    
    Wallet = {}
    Wallet[0] = [[]]
    for j in range(1, amount+1):
        for i in range(0, len(coins)):
            if(coins[i]<=j and j-coins[i]>=0):
                remain_amount = j - coins[i]
                if j not in Wallet:
                    Wallet[j] = []
                if remain_amount in Wallet:
                    for a in Wallet[remain_amount]:
                        temp = list(a)
                        temp.append(coins[i])
                        temp.sort()
                        if temp not in Wallet[j]:
                            Wallet[j].append(temp)
                            print(Wallet)

    for keys,values in Wallet.items():
        print(keys)
        print(values)
    
    print("The number of ways to make an amount {} are/is {}".format(amount, len(Wallet[amount])))

'''
LeetCode solution and it works
def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j-coins[i] >= 0:
                    dp[j] += dp[j-coins[i]]
        return dp[amount]
'''


amount = 5 
coins = [1,2,5]
makeCoinChanges(amount, coins)

# amount = 5
# coins = [2]
# makeCoinChanges(amount, coins)

# amount = 10
# coins = [10]
# makeCoinChanges(amount, coins)

# amount = 10
# coins = [5]
# makeCoinChanges(amount, coins)

# makeCoinChanges(500, [1,2,5])

