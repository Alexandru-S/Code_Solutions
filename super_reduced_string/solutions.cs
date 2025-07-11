    public static string superReducedString(string s)
    {
        for(int i= s.Length-1;i >0; i--){
            if(s[i] == s[i-1]){
                s = s.Remove(i-1,2);
                i = s.Length;
            }
        }
        if(s.Length == 0){
            return "Empty String";
        }else{
            return s;
        }

    }