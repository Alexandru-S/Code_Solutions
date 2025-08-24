 static bool IsPrime(int num)
    {
        if (num < 2) return false;
        if (num % 2 == 0) return num == 2;
        int limit = (int)Math.Sqrt(num);
        for (int i = 3; i <= limit; i += 2)
            if (num % i == 0) return false;
        return true;
    }

    static List<int> FirstQPrimes(int q)
    {
        var primes = new List<int>(q);
        int n = 2;
        while (primes.Count < q)
        {
            if (IsPrime(n)) primes.Add(n);
            n++;
        }
        return primes;
    }

    // ---- Main task ----
    // number: initial plate stack A0 given as a list (left->right = bottom->top)
    // q: number of iterations
    public static List<int> waiter(List<int> number, int q)
    {
        var primes = FirstQPrimes(q);
        // A0 top is the last element of 'number'
        var A = new Stack<int>(number); // ctor preserves top as last element of the IEnumerable

        var answer = new List<int>(number.Count);

        for (int i = 0; i < q; i++)
        {
            int p = primes[i];
            var nextA = new Stack<int>();
            var B = new Stack<int>();

            // Pop all from current A
            while (A.Count > 0)
            {
                int x = A.Pop();
                if (x % p == 0) B.Push(x);
                else nextA.Push(x);
            }

            // Append B_i top->bottom to answer
            while (B.Count > 0)
                answer.Add(B.Pop());

            // A becomes A_{i+1}
            A = nextA;
        }

        // After q rounds, dump remaining A_q top->bottom
        while (A.Count > 0)
            answer.Add(A.Pop());

        return answer;
    }