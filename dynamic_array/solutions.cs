    public static List<int> dynamicArray(int n, List<List<int>> queries){
        int [][] arr = new int [n][];
        List<int> result = new List<int>();
        for(int i = 0 ; i< n ; i++){
            arr[i] = new int[0];
        }
        int lastAnswer = 0;
        Console.WriteLine("wgwrgwrgw"+queries.Count);
        for(int i =0; i<queries.Count; i++){
            Console.WriteLine("-*9-*-*-*-*-*-*-*-*-**1-"+queries[i][0]);
            Console.WriteLine("-*9-*-*-*-*-*-*-*-*-**2-"+queries[i][1]);
            Console.WriteLine("-*9-*-*-*-*-*-*-*-*-**3-"+queries[i][2]);
            int idx = (queries[0][2]^lastAnswer) %n;
            if(queries[i][0] == 1){    
                lastAnswer = idx;
                arr[idx].Append(queries[i][2]);
            }
            if(queries[i][0]== 2){
                lastAnswer = arr[idx][queries[i][2]%arr[idx].Length];
                result.Add(lastAnswer);
            }
        }
        Console.Write("*-*--**-*-*"+result.Count);
        return result;
    }