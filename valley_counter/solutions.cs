    public static int countingValleys(int steps, string path)
    {
        int valleys = 0;
        int alt = 0;
        for(int i = 0; i<steps; i++){
            if(path[i] == 'D'){
                alt -=1;
            }else if(path[i] == 'U'){
                alt +=1;
            }
            if(alt ==0 && path[i] == 'U'){
                valleys++;
            }      
        }
        return valleys; 
    }