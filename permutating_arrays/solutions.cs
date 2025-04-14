public static string twoArrays(int k, List<int> A, List<int> B)
    {
        A.Sort();
        B.Sort((a,b)=>b.CompareTo(a));
        
            for(int i = 0 ; i< A.Count; i++){
                if(A[i] + B[i] < k){
                    return "NO";
                }
            }
        return "YES";
    }