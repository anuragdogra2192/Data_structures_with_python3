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
"""


def coinChange(amount, coins):
    coins.sort(reverse=True)
    print(coins)
    reach_amount  = amount
    main_coin_id = 0
    coin_idx = 0
    wallet = []
    temp = []
    if amount == 0:
        return 0
    
    while reach_amount <= amount and main_coin_id < len(coins):
        if reach_amount >= coins[coin_idx]:
            temp.append(coins[coin_idx])
            #print(temp)
            reach_amount = reach_amount - coins[coin_idx]
            #print("RA: {} with coin {}.".format(reach_amount, coins[coin_idx]))

        elif reach_amount == 0 and main_coin_id < len(coins):
            wallet.append(temp)
            temp = []
            main_coin_id += 1
            reach_amount = amount
            #print("Reset_amount: {} and main coin: {}".format(reach_amount, coins[main_coin_id]))
            coin_idx = main_coin_id       
        else:
            coin_idx+=1        

    if wallet == []:
        return -1
    print(max(wallet))        
    return len(max(wallet))

print("Minimum number of coins:", coinChange(11,[2,5,1]))

