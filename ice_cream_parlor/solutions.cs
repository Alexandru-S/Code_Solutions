public static List<int> icecreamParlor(int m, List<int> arr)
{
    Dictionary<int, int> priceTrack = new Dictionary<int, int>();

    for (int i = 0; i < arr.Count; i++)
    {
        int cost = arr[i];
        int complement = m - cost;

        if (priceTrack.ContainsKey(complement))
        {
            return new List<int> { priceTrack[complement], i + 1 }; 
        }

        if (!priceTrack.ContainsKey(cost))
            priceTrack[cost] = i + 1; 
    }

    return new List<int>();
}