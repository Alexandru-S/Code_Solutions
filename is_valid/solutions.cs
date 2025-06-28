    public static string isValid(string s)
    {
        var charTrack = new Dictionary<char, int>();
        foreach(char x in s){
            charTrack[x] = charTrack.TryGetValue(x, out var c)? c+1 :1;
        }
        var freqTrack = new Dictionary<int, int>();
        foreach(var y in charTrack){
            freqTrack[y.Value] = freqTrack.TryGetValue(y.Value, out var c)? c+1:1; 
        }
        if(freqTrack.Count == 1){
            return "YES";
        }
        if(freqTrack.Count == 2){
            var keys = freqTrack.Keys.ToList();
            int freq1 = keys[0];
            int freq2 = keys[1];
            int count1 = freqTrack[freq1];
            int count2 = freqTrack[freq2];
            
            if((freq1 == 1 && count1 == 1)||(freq2 == 1 && count2 == 1)){
                return "YES";
            }
            if((Math.Abs(freq1-freq2) == 1)&&(count1 == 1 || count2 == 1)){
                return "YES";
            }
            return "NO";
        }
        
        return "NO";
        
    }
