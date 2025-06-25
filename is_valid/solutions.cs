    public static string isValid(string s)
    {
        char[] charArray = s.ToCharArray();
        var letterTrack = new Dictionary<char,int>();
        foreach(char x in charArray ){
            letterTrack[x] = letterTrack.TryGetValue(x, out var c)? c+1: 1;
        }
        

    }