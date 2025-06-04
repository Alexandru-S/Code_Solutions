    public static void countSort(List<List<string>> arr)
    {
        List<string>[] dashedList = new List<string>[100];
        for (int i = 0; i < 100; i++)
        {
            dashedList[i] = new List<string>();
        }
        int halfWay = arr.Count/2;
        for(int i = 0; i< arr.Count; i++){
            int index = int.Parse(arr[i][0]);
            string value = i < halfWay ? "-": arr[i][1];
            dashedList[index].Add(value);
        }
        StringBuilder output = new StringBuilder();
        foreach( var minilist in dashedList){
            foreach(var value in minilist){
                output.Append(value).Append(" ");
            }
        }
        Console.Write(output);
    }
