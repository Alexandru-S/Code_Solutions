    public static void plusMinus(List<int> arr){
        int arrLength = arr.Count;
        int sumOfPositive = 0;
        int sumOfNegative = 0;
        int sumOfZero = 0;
        for(int i = 0 ; i < arrLength; i++){
            if(arr[i] == 0){
                sumOfZero++;
            }else if(arr[i] > 0){
                sumOfPositive++;
            }else{
                sumOfNegative++;
            }
        }
        double posResult = (double) sumOfPositive/arrLength;
        double negResult = (double) sumOfNegative/arrLength;
        double zeroResult = (double) sumOfZero/arrLength;
        Console.WriteLine(posResult.ToString("F6"));
        Console.WriteLine(negResult.ToString("F6"));
        Console.WriteLine(zeroResult.ToString("F6"));
    }