    public static void separateNumbers(string s){
        if(s.Length == 1 || s[0] == '0'){
            Console.WriteLine("NO");
        }else{
            for(int i = 0 ; i< s.Length/2; i++){
                int sampleInt = int.Parse(s.Substring(0,i+1).ToString());
                string sampleSequence = sampleInt.ToString();
                var sb = new StringBuilder();
                int arrayLength = sampleInt+(s.Length/(i+1));
                for(int j = sampleInt; j<sampleInt+(s.Length/(i+1)); j++){
                    sb.Append(j);
                    if(sb.ToString().Length == s.Length){
                        break;
                    }
                } 
                if(sb.ToString() ==s){
                    Console.WriteLine("YES "+ sampleInt);
                    break;
                }else if(sb.ToString() != s && i == (s.Length/2)-1){
                    Console.WriteLine("NO");
                    break;
                }
            }
        }

    }