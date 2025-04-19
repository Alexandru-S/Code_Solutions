    public static int pickingNumbers(List<int> a)
    {
        var numberTrack = new Dictionary<int,int>();
        foreach(var x in a){
            numberTrack[x] = numberTrack.TryGetValue(x, out var c) ? c+1 : 1;
        }
        var reordered = numberTrack.OrderBy(kv => kv.Key).ToList();
        int largestCount = 0;
        int lastCount = 0;
        if(reordered.Count == 1){
            return reordered[0].Value;
        }
        for(int i = 0; i< reordered.Count-1;i++){
            lastCount = reordered[i+1].Value;
            if(reordered[i+1].Key - reordered[i].Key ==1){
                lastCount = reordered[i+1].Value + reordered[i].Value;
            }
            if(lastCount > largestCount){
                largestCount = lastCount;
            }
        }
        return largestCount;
    }