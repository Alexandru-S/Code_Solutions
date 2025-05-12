    public static List<int> missingNumbers(List<int> arr, List<int> brr)
    {
        var freqA = new Dictionary<int,int>();
        var freqB = new Dictionary<int,int>();
        foreach(var x in arr){
            freqA[x] = freqA.TryGetValue(x, out var c) ? c+1 : 1;
        }
        foreach(var x in brr){
            freqB[x] = freqB.TryGetValue(x, out var c) ? c+1 : 1;
        }
        var missing = new List<int>();
        foreach(var kv in freqB){
            int num = kv.Key;
            int countInB = kv.Value;
            freqA.TryGetValue(num, out int countInA );
            if(countInB > countInA){
                missing.Add(num);
            }
        }
        missing.Sort();
        return missing;
    }