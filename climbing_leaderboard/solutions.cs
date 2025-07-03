 public static List<int> climbingLeaderboard(List<int> ranked, List<int> player)
    {
        List<int> result = new List<int>();
        Dictionary<int, int> rankedScores = ranked.Distinct().OrderByDescending(score => score).Select((score, index) => new { score, rank = index + 1 }).ToDictionary(x => x.score, x => x.rank);
        for(int i = 0; i<player.Count; i++){
            Boolean foundplace = false;
            int position = 0;
            while(!foundplace){
                if(rankedScores[position] ==player[i] ){
                    foundplace =true;
                    result[i] = rankedScores[position];
                }else if()
            }
            
        }
        return result;
    }