    public static List<int> closestNumbers(List<int> arr)
    {
        arr.Sort();
        int minimumDifference = Int32.MaxValue;
        for(int i = 0; i< arr.Count -1; i++){
            if(arr[i+1] - arr[i] < minimumDifference){
                minimumDifference = arr[i+1]-arr[i];
            }
        }
        List<int> returnList= new List<int>();
        for(int i =0; i < arr.Count-1;i++){
            if(arr[i+1]-arr[i] == minimumDifference){
                returnList.Add(arr[i]);
                returnList.Add(arr[i+1]);
            }
        }
        return returnList;
    }