   public static string balancedSums(List<int> arr)
    {
        int totalSum = arr.Sum();
        int LeftSum = 0;
        for(int i = 0; i< arr.Count; i++){
            int rightSum = totalSum-LeftSum-arr[i];
            if(LeftSum == rightSum){
                return "YES";
            }
            LeftSum+=arr[i];
        }
        return "NO";

    }