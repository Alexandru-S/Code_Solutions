
    static bool isPrime(int num){
        if(num < 2) return false;
        if(num == 2 || num == 3) return true;
        if(num % 2 == 0) return false;
        int limit = (int) Math.Sqrt(num);
        for(int i =2; i< limit; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
    
    static int getNextPrime(int n){
        while(!isPrime(n)){
            n++;
        }
        return n;
    }
    
    static List<int> GetPrimesUpTo(int limit){
        if(limit < 2) return new List<int>();
        bool [] isComposite = new bool[limit +1];
        List<int> primes = new List<int>();
        for(int i =0; i<= limit ; i++){
            if(!isComposite[i]){
                primes.Add(i);
                for(int j = i*2;j<=limit; j+=i ){
                    isComposite[j] = true;
                }
            }
        }
        return primes;
    }
 
    public static List<int> waiter(List<int> number, int q)
    {
        int highestPrime = getNextPrime(number.Max());
        List<int> primes = GetPrimesUpTo(highestPrime);
        Stack<int> stackA =  new Stack<int>(number);
        Stack<int> stackB = new Stack<int>();
        List<int> answers = new List<int>(number.Count);
       for (int i = 0; i < q; i++)
        {
            int p = primes[i];
            var nextA = new Stack<int>();
            var B = new Stack<int>();
            // Pop all from current A
            while (stackA.Count > 0)
            {
                int x = stackA.Pop();
                if (x % p == 0) B.Push(x);
                else nextA.Push(x);
            }
            // Append B_i top->bottom to answer
            while (B.Count > 0)
                answers.Add(B.Pop());

            // A becomes A_{i+1}
            stackA = nextA;
        }

        // After q rounds, dump remaining A_q top->bottom
        while (stackA.Count > 0)
            answers.Add(stackA.Pop());

        return answers;
        

    }