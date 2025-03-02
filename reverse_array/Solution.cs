    public static List<int> reverseArray(List<int> a)
    {
        int positionPointer = a.Count();
        int halfwayPoint = (positionPointer/2);
        for(int i = 0 ; i<a.Count() - 1; i++){
            if(i == halfwayPoint){break;}
            positionPointer--;
            int replaceFirst = a[i];
            a[i] = a[positionPointer];
            a[positionPointer] = replaceFirst;
        }
        return a;
    }