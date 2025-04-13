    public static string pangrams(string s)
    {
        var result = s.ToLower().Where(char.IsLetter).Distinct();
        if(result.Count() == 26){
            return "pangram";
        }else{
            return "not pangram";
        }
    }