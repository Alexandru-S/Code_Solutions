    public static int lonelyinteger(List<int> a){
        return a.Find(x => a.Count(j => x ==j) == 1);
    }
