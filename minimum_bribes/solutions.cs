    public static void minimumBribes(List<int> q)
    {
        int count = 0;
        int maxNumber = q.Max();
        bool tooChaotic = false;
        List<int> originalQ = Enumerable.Range(1,maxNumber).ToList();
        for(int i = 0; i < originalQ.Count; i++){
            if(originalQ[i] < q[i]){
                if(q[i]- originalQ[i] > 2){
                    tooChaotic = true;
                    break;
                }
                count+= q[i]-originalQ[i];
            }
        }
        if(tooChaotic){
            Console.WriteLine("Too chaotic");
        }else{
            Console.WriteLine(count);
        }
    }