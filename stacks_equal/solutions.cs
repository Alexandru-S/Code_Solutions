    public static List<int> createPossibleHeights(List<int> hn){
        HashSet<int> possible_height = new HashSet<int>{0};
        for(int i = 0; i<hn.Count; i++){
            var newHeights = possible_height.Select(sum => sum + hn[i]).ToList();
            for(int j = 0; j< newHeights.Count; j++){
                possible_height.Add(newHeights[j]);
            }
        }
        List<int> sortedHeights = possible_height.OrderBy(x => x).ToList();
        return sortedHeights;
    }

    public static int equalStacks(List<int> h1, List<int> h2, List<int> h3)
    {
        int h1_height = h1.Sum();
        int h2_height = h2.Sum();
        int h3_height = h3.Sum();
        
        
        
        if(h2_height == h1_height && h3_height == h1_height){
            return h1_height;
        }
        int min_height = Math.Min(h1_height, Math.Min(h2_height,h3_height));
        int possible_height_h1 = createPossibleHeights(h1);
        int possible_height_h2 = createPossibleHeights(h2);
        int possible_height_h3 = createPossibleHeights(h3);
        

    }