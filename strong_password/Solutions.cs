public static int minimumNumber(int n, string password)
    {
        string numbers = "0123456789";
        string lower_case = "abcdefghijklmnopqrstuvwxyz";
        string upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string special_characters = "!@#$%^&*()-+";
        int result = 0;
        
        var passwordHash = new HashSet<char>(password);
        bool matchSpecial = special_characters.Any(passwordHash.Contains);
        bool matchUpper = upper_case.Any(passwordHash.Contains);
        bool matchLower = lower_case.Any(passwordHash.Contains);
        bool matchNumbers = numbers.Any(passwordHash.Contains);
        if(!matchSpecial){
            result += 1;
        }
        if(!matchUpper){
            result += 1;
        }
        if(!matchNumbers){
            result += 1;
        }
        if(!matchLower){
            result+= 1;
        }
        if(password.Length+result <6){
            result +=6-password.Length-result;
        }
        
        return result;
    }