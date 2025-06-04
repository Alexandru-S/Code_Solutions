// important, this should be calculated with something using linear time
// So instead of generating all subarrays, use a mathematical observation to solve it in linear time
// Observation = find frequency using i + 1) * (n - i) if its even it cancels out if its odd XOR it

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
