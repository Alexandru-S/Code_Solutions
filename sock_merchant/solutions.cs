    public static int sockMerchant(int n, List<int> ar)
    {
        var matchCheck = new Dictionary<int, int>();
        for(int i = 0; i< n; i++){
            if(!matchCheck.TryGetValue(ar[i], out var count)){
                count =0;
            }
            matchCheck[ar[i]]= count+1;
        }
        int countPairs= 0;
        foreach(var x in matchCheck){
            if(x.Value >1){
                countPairs += x.Value/2;
            }
        }
        return countPairs; 
    }