    public static string isBalanced(string s)
    {
        List<char> opening = new List<char>{'(','{','['};
        List<char> closing = new List<char>{')','}',']'};
        List<char> charList = s.ToList();
        Stack<char> compare = new Stack<char>();
        for(int i = 0; i< charList.Count; i++){
            if(opening.Contains(charList[i])){
                compare.Push(charList[i]);
            }else{
                if(compare.Count == 0){
                    return "NO";
                    break;
                }
                char lastOpeningBracket = compare.Peek();
                int indexofLastBracket = opening.IndexOf(lastOpeningBracket);
                if(closing[indexofLastBracket] != charList[i]){
                    return "NO";
                    break;
                }else{
                    compare.Pop();
                }
            }
            
        }
        return "YES";

    }