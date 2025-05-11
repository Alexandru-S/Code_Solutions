public static int maxMin(int k, List<int> arr)
{
    arr.Sort();
    int minimumDiff = Int32.MaxValue;
    for(int i = 0; i< arr.Count-k+1; i++){
        int localMinimum = arr[i+k-1]-arr[i];            
        if(localMinimum<minimumDiff){
            minimumDiff = localMinimum;
        }
    }
    return minimumDiff;

}