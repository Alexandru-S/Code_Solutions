public static void separateNumbers(string s){
        int n = s.Length;
        if(s.Length == 1 || s[0] == '0'){
            Console.WriteLine("NO");
            return;
        }else{
            for(int i = 1 ; i<= n/2; i++){
                long sampleInt = long.Parse(s.Substring(0,i).ToString());
                string sampleSequence = sampleInt.ToString();
                var sb = new StringBuilder();
                long arrayLength = sampleInt+(n/(i));
                for(long j = sampleInt; j<sampleInt+(n/i); j++){
                    sb.Append(j);
                    if(sb.ToString().Length == n){
                        break;
                    }
                } 
                if(sb.ToString() ==s){
                    Console.WriteLine("YES "+ sampleInt);
                    break;
                }else if(sb.ToString() != s && i == (n/2)){
                    Console.WriteLine("NO");
                    break;
                }
            }
        }

    }