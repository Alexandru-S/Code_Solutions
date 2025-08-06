public static long stockmax(List<int> prices){
    long profit = 0;
    int maxPriceSoFar = 0;
    for(int i = prices.Count -1; i>=0; i--){
        if(prices[i] > maxPriceSoFar){
            maxPriceSoFar = prices[i];
        }
        profit += maxPriceSoFar - prices[i];
    }
    return profit;
}