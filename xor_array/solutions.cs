     public static int sansaXor(List<int> arr)
    {
        int result = 0;
        int n = arr.Count;
        for(int i = 0; i < n; i++){
            long frequency = (long)(i + 1) * (n - i);
            if(frequency %2 != 0){
               result ^=arr[i]; 
            }
        }
        return result;
    }
