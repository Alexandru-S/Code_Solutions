    // Function designed to miror a matrix
    public static List<List<int>> reflect(List<List<int>> arr){
        List<List<int>> rft = new List<List<int>>();
        foreach(int i in Enumerable.Range(0,3)){
            List<int> lst = new List<int>();
            foreach(int j in Enumerable.Range(0,3).Reverse()){
                lst.Add(arr[i][j]);
            }
            rft.Add(lst);
        }
        return rft;
    }
    // Function designed to rotate a matrix
    public static List<List<int>> rotate(List<List<int>> arr){
        List<List<int>> rot = new List<List<int>>();
        foreach(int j in Enumerable.Range(0,3)){
            List<int> lst = new List<int>();
            Console.WriteLine(arr[j].Count());
            foreach(int i in Enumerable.Range(0,3).Reverse()){
                lst.Add(arr[i][j]);
            }
            rot.Add(lst);
        }
        return rot;
    }
    // Function designed to count the totals of a row
    public static int total(List<List<int>> s, List<List<int>> arr){
        List<int> total = new List<int>();
        foreach(int row in Enumerable.Range(0,3)){
            List<int> totalRow = new List<int>();
            foreach(int col in Enumerable.Range(0,3)){
                totalRow.Add(Math.Abs(s[row][col]-arr[row][col]));
            }
            total.Add(totalRow.Sum());
        }
        return total.Sum();
    } 

    // Checking how close the matrix s is to beaing a perfect matrix, one of 8 posibilities involving ms
    public static int formingMagicSquare(List<List<int>> s){
        List<List<int>> ms = new List<List<int>> {
            new List<int> { 4, 3, 8 },
            new List<int> { 9, 5, 1 },
            new List<int> { 2, 7, 6 }
        };
        List<int> totals = new List<int>();
        foreach( int tot in Enumerable.Range(0,4)){
            totals.Add(total(s,ms));
            List<List<int>> refrenceMagicSquare = reflect(ms);
            totals.Add(total(s, refrenceMagicSquare));
            ms = rotate(ms);
        }
        return totals.Min();
    }
