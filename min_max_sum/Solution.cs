    public static void miniMaxSum(List<int> arr){
        arr.Sort();
        long minimumSum = arr.Take(4).Select(x => (long)x).Sum();
        long maximumSum = arr.Skip(Math.Max(0, arr.Count-4)).Select(x => (long)x).Sum();
        Console.Write("{0} {1}",minimumSum,maximumSum);
    }