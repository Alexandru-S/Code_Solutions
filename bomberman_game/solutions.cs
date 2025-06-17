public static List<string> bomberMan(int n, List<string> grid)
    {
        if(n == 1){
            return grid;
        }
        List<string> filledGrid = Enumerable.Repeat( new string('O',grid[0].Length ), grid.Count).ToList();
        if(n % 2 == 0){
          return filledGrid;  
        }
        else if(n %4 == 3){
            return bomberLocations(grid, filledGrid);
        }else{
            var full = Enumerable.Repeat(new string('O', grid[0].Length), grid.Count).ToList();
            return bomberLocations(bomberLocations(grid, filledGrid), full);
        }
    }
    
    public static List<string> bomberLocations(List<string> grid, List<string> plantedGrid){
        for(int i = 0; i< grid.Count; i++){
            for(int j = 0; j<grid[i].Length; j++){
                if(grid[i][j] == 'O'){
                    char[] charsi = plantedGrid[i].ToCharArray();
                    charsi[j] = '.';
                    plantedGrid[i] = new string(charsi);
                    if(i > 0){
                        if(grid[i-1][j] != 'O'){
                            char [] chars = plantedGrid[i-1].ToCharArray();
                            chars[j] = '.';
                            plantedGrid[i-1] = new string(chars);
                        }
                    }
                    if(i < grid.Count-1){
                        if(grid[i+1][j] != 'O'){
                            char [] charsbottom = plantedGrid[i+1].ToCharArray();
                            charsbottom[j] = '.';
                            plantedGrid[i+1] = new string(charsbottom);
                        }
                    }
                    if(j > 0){
                        if(grid[i][j-1] != 'O'){
                            char [] charsLeft = plantedGrid[i].ToCharArray();
                            charsLeft[j-1] = '.';
                            plantedGrid[i] = new string(charsLeft);
                        }
                    }
                    if(j < grid[i].Length-1){
                        if(grid[i][j+1] != 'O'){
                            char [] charsRight = plantedGrid[i].ToCharArray();
                            charsRight[j+1] = '.';
                            plantedGrid[i] = new string(charsRight);
                        }
                    }
                }
            }
        }
        return plantedGrid;
    }