public static int sherlockAndAnagrams(string s)
{
    Dictionary<string, int> subStringCounts = new Dictionary<string, int>();
    for (int i = 0; i < s.Length; i++) {
        for (int j = 1; j <= s.Length - i; j++) {
            string substring = s.Substring(i, j);
            string sorted = String.Concat(substring.OrderBy(c => c));
            if (subStringCounts.ContainsKey(sorted)) {
                subStringCounts[sorted]++;
            } else {
                subStringCoSunts[sorted] = 1;
            }
        }
    }
    int count = 0;
    foreach (var kvp in subStringCounts) {
        int freq = kvp.Value;
        if (freq > 1) {
            count += (freq * (freq - 1)) / 2;
        }
    }
    return count;

}
