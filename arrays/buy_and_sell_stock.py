from typing import List

def buy_and_sell_stock(prices: List[int]) -> int:
    profit = 0
    i = 1

    while i < len(prices):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

        i += 1

    return profit
    
if __name__ == '__main__':
    print(buy_and_sell_stock([1, 7, 2, 3, 6, 7, 6, 7]))


