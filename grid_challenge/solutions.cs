    public static string gridChallenge(List<string> grid)
    {
        for(var i = 0; i< grid.Count; i++){
            char[] original = grid[i].ToCharArray();
            char[] sorted = (char[])original.Clone();
            Array.Sort(sorted);
            if(!original.SequenceEqual(sorted)){
                grid[i] = new string(sorted);
            }
        }
        for(var i = 0; i< grid[0].Length; i++){
            var stringColumn = "";
            for(var j = 0; j < grid.Count; j++){
                stringColumn+=(grid[j][i]);
            }
            char[] original = stringColumn.ToCharArray();
            char[] sorted = (char[])original.Clone();
            Array.Sort(sorted);
            if(!original.SequenceEqual(sorted)){
                return "NO";
            }            
        }
        return "YES";
    }
