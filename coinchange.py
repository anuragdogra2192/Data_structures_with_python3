def coinChange(vector<int>& coins, int amount):
    NumForAmount = [0]*amount
    Wallet[0] = {}
    for j in range(1,len(amount)):
        for i in range(0, len(coins)):
            if(coins[i]<j):
                NumForAmount[j] = min(NumForAmount[j], NumForAmount[j-coins[i]])
                if amount in Wallet:
                    Wallet[amount] = []
                else:
                    Wallet[amount] = []



coins = [1,2,5]
amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1