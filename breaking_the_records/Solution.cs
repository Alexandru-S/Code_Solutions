public static List<int> breakingRecords(List<int> scores)
    {
        int highestScore = scores[0];
        int lowestScore = scores[0];
        int highestCount = 0;
        int lowestCount = 0;
        for(int i = 1; i<scores.Count; i++){
            if(scores[i] > highestScore){
                highestScore = scores[i];
                highestCount++;
            }
            if(scores[i] < lowestScore){
                lowestScore = scores[i];
                lowestCount++;
            }
        }
        return [highestCount,lowestCount];

    }