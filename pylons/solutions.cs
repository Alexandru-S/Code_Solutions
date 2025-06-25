    public static int pylons(int k, List<int> arr)
    {
        int n = arr.Count;
        int count = 0;
        int i = 0;
        int loc = i + k -1;
        while(i < n){
            if(arr[loc] == 1){
                count += 1;
                i = loc+k;
                loc = i + k -1;
                if(loc >= n){
                    loc = n-1;
                }
            }else{
                loc -= 1;
                if(loc < 0 || loc < i - k +1){
                   return -1; 
                }
            }
        }
        return count;

    }