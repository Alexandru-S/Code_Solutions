// special case is when all the piles are 1
// other than that, check to see if the piles XOR
// if XOR result is not zero, its the first player who wins
// ptherwise its the third
public static string misereNim(List<int> s)
    {
        int n = s.Count;
        bool allOnes = s.All(x => x ==1);
        if(allOnes && n%2 ==1 ){
            return "Second";
        }
        else if(allOnes && n%2 == 0){
            return "First";
        }
        else if(s.Aggregate((x,y) => x^y) != 0){
            return "First";
        }
        else{
            return "Second";
        }

    }
