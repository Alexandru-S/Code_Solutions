public static List<int> createPossibleHeights(List<int> hn){
    HashSet<int> possible_height = new HashSet<int>();
    int maxHeight = hn.Sum();
    possible_height.Add(maxHeight);
    for(int i = 0; i< hn.Count; i++){
        maxHeight -= hn[i];
        possible_height.Add(maxHeight);
    }
    return possible_height.ToList();
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
    List<int> possible_height_h1 = createPossibleHeights(h1);
    List<int> possible_height_h2 = createPossibleHeights(h2);
    List<int> possible_height_h3 = createPossibleHeights(h3);
    var common = possible_height_h1.Intersect(possible_height_h2).Intersect(possible_height_h3);
    if(common.Any()){
        return common.Max();
    }
    return 0;

}