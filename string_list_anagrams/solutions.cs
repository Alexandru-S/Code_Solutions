
public static int sherlockAndAnagrams(string s)
{
    List<string> allSubStrings = new List<string>();
    for(int i =0; i<s.Length; i++){
        for(int j = 1; j<=s.Length-i; j++){
            string substring = s.Substring(i,j);
            string sorted = String.Concat(substring.OrderBy(c => c));
            allSubStrings.Add(sorted);
        }
    }
    allSubStrings.Sort();
    int listLength = allSubStrings.Count;
    int count = 0;
    for(int i = listLength-1; i>0; i--){
            if(allSubStrings[i] == allSubStrings[i-1]){
            allSubStrings.RemoveAt(i);
            allSubStrings.RemoveAt(i-1);
            listLength = allSubStrings.Count;
            count++;
            }
    }
    return count;

}