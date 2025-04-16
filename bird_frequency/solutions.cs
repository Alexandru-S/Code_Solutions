    public static int migratoryBirds(List<int> arr)
    {
        int arrLength = arr.Count;
        var trackBirds = new Dictionary<int,int>();
        foreach(var x in arr){
            trackBirds[x] = trackBirds.TryGetValue(x, out var c) ? c+1 : 1;
        }

        var minEntry = trackBirds.OrderByDescending(kv => kv.Value).ThenBy(kv => kv.Key).First();
        return minEntry.Key;
    }