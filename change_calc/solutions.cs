    public static long getWays(int n, List<long> c)
    {
        c.Sort();
        long count = 0;
        
        void Dfs(int start , long remaining){
            if(remaining == 0){
                count++;
                return;
            }
            for(int i = start; i< c.Count; i++){
                long coin = c[i];
                if(coin > remaining){
                    break;
                }
                Dfs(i, remaining - coin);
            }
        }
        
        Dfs(0 , n);
        return count;
    }