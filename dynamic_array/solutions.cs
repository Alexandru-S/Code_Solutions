    public static List<int> dynamicArray(int n, List<List<int>> queries){
        int [][] arr = new int [n][];
        List<int> result = new List<int>();
        for(int i = 0 ; i< n ; i++){
            arr[i] = new int[0];
        }
        int lastAnswer = 0;
        for(int i =0; i<queries.Count; i++){
            int idx = (queries[i][1] ^ lastAnswer) % n;
            if(queries[i][0] == 1){   
                   int val = queries[i][2];
                    Array.Resize(ref arr[idx], arr[idx].Length + 1);
                    arr[idx][ arr[idx].Length - 1 ] = val;
            }
            if(queries[i][0]== 2){      
                lastAnswer = arr[idx].Length > 0 ? arr[idx][ queries[i][2] % arr[idx].Length ]: 0;
                result.Add(lastAnswer);
            }
        }
        return result;
    }