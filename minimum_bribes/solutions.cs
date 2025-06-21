 public static void minimumBribes(List<int> q)
{
    int count = 0;
    for (int i = 0; i < q.Count; i++)
    {
        if (q[i] - (i + 1) > 2)
        {
            Console.WriteLine("Too chaotic");
            return;
        }
        for (int j = Math.Max(0, q[i] - 2); j < i; j++)
        {
            if (q[j] > q[i])
            {
                count++;
            }
        }
    }

    Console.WriteLine(count);
}
