    public static List<int> rotateLeft(int d, List<int> arr)
    {
        int n = arr.Count;
        int shift = d;
        if(d>n){
            shift =  d%n;
        }
        List<int> leftSide = arr.GetRange(0, shift);
        List<int> rightSide = arr.GetRange(shift, n-shift);
        return rightSide.Concat(leftSide).ToList();

    }