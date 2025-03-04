    public static string timeConversion(string s){
        DateTime dt = DateTime.Parse(s);
        return dt.ToString("HH:mm:ss");
    }