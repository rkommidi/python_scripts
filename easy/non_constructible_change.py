#Non-Construcible Change
# if you're given coins = [1,2,5], the minimum amount of change that you can't create is 4. if you are given no coins, the min that you can't create is 1.

# coins = [5,7,1,1,2,3,22]
#output = 20


#O(nlogn) time | O(1) space - n is number of coins

def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0 
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1
