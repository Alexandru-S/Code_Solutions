    public static List<int> climbingLeaderboard(List<int> ranked, List<int> player)
    {
        List<int> result = new List<int>();
        ranked = ranked.Distinct().ToList();
        ranked.Sort();
        int n = ranked.Count;
        Console.WriteLine("n leangth"+n);
        int i = 0;
        foreach(int score in player){
            while( i<n && ranked[i] <= score ){
                i++;
            }
            result.Add(n-i+1);
        }
        return result;
    }
