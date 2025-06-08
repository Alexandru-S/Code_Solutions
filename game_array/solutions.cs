
    public static string gamingArray(List<int> arr)
    {
        int count = 0;
        while(arr.Count != 0){
            int currentMax = arr.Max();
            int indexMax = arr.IndexOf(currentMax);
            arr.RemoveRange(indexMax, arr.Count - indexMax);
            count++;
        }
        if(count%2 ==0){
            return "ANDY";
        }else{
            return "BOB";
        }

    }
