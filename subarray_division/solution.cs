    public static int birthday(List<int> s, int d, int m){
        int count = 0; 
        for(int i = 0 ; i < s.Count -m+1; i++){
            int tempCount = 0;
            for(int j = i ; j < i+m ; j++){
                tempCount += s[j];
            }
            if(tempCount == d){
                count++;
            }
        }
        return count;
    }