# time complexity O(n) , space complexity O(1)


def buySellOptimizer(stock_prices):
    """
    A function that calculates the best times to buy and sell
    a product given variable stock_prices



    Args:
        stock_prices (dict): contains a dictionary of the days
        and respective prices in those days

    Returns:
        String: Buy[n]Sell[n+m]
    """
    max_profit = 0  # max profit tracker
    min_day = 32000  # min profit tracker
    buy = 0  # buy day tracker
    sell = 0  # sell day tracker
    for ticket in stock_prices:
        if ticket["Price"] < min_day:
            buy = ticket["Day"]
        min_day = min(min_day, ticket["Price"])
        if ticket["Price"] - min_day > max_profit:
            sell = ticket["Day"]
        max_profit = max(max_profit, ticket["Price"] - min_day)
    return_string = (
        "Buy[" + str(buy) + "]Sell[" + str(sell) + "]"
    )  # concat results in requested format
    return return_string


stock_prices = [
    {"Day": 0, "Price": 5},
    {"Day": 1, "Price": 9},
    {"Day": 2, "Price": 3},
    {"Day": 3, "Price": 5},
    {"Day": 4, "Price": 8},
    {"Day": 5, "Price": 7},
]

print(buySellOptimizer(stock_prices))
