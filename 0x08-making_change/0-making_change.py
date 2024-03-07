#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''

import sys

def makeChange(coins, total):
    '''
    Return the fewest number of coins needed to meet the total amount.
    If the total is 0 or less, return 0.
    If the total cannot be met by any combination of coins, return -1.
    '''
    if total <= 0:
        return 0

    
    min_coins = [sys.maxsize] * (total + 1)
    min_coins[0] = 0

    # Iterate through each total amount from 1 to the given total
    for amount in range(1, total + 1):
        for coin in coins:
            
            # Calculate the number of coins needed for the remaining amount
            remaining = amount - coin
            sub_result = min_coins[remaining]
            # Update the minimum number of coins if the current combination requires fewer coins
            if sub_result != sys.maxsize and sub_result + 1 < min_coins[amount]:
                    min_coins[amount] = sub_result + 1

    # If the minimum number of coins for the total amount is still sys.maxsize, it means the total cannot be met
    if min_coins[total] == sys.maxsize:
        return -1

    return min_coins[total]
