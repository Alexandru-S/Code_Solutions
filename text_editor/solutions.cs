 static void Main(String[] args) {
 int q = int.Parse(Console.ReadLine()!);
        var s = new StringBuilder();
        var undo = new Stack<Tuple<int, string>>();

        for (int i = 0; i < q; i++)
        {
            string[] parts = Console.ReadLine()!.Split(' ', 2);
            int op = int.Parse(parts[0]);

            switch (op)
            {
                case 1:
                    string x = parts[1];
                    s.Append(x);
                    undo.Push(Tuple.Create(1, x.Length.ToString()));
                    break;

                case 2:
                    int k = int.Parse(parts[1]);
                    int start = s.Length - k;
                    string deleted = s.ToString(start, k);
                    s.Length = start;
                    undo.Push(Tuple.Create(2, deleted));
                    break;

                case 3:
                    int idx = int.Parse(parts[1]);
                    Console.WriteLine(s[idx - 1]);
                    break;

                case 4:
                    if (undo.Count > 0)
                    {
                        var last = undo.Pop();
                        if (last.Item1 == 1)
                        {
                            int len = int.Parse(last.Item2);
                            s.Length = s.Length - len;
                        }
                        else
                        {
                            s.Append(last.Item2);
                        }
                    }
                    break;
            }
        }
    }