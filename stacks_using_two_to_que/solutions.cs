using System;
using System.Collections.Generic;

class Solution
{    static void Main(String[] args)
    {
        int q = Convert.ToInt32(Console.ReadLine());
        Queue queue = new Queue();

        for (int i = 0; i < q; i++)
        {
            string[] input = Console.ReadLine().Split(' ');

            int type = Convert.ToInt32(input[0]);

            if (type == 1)
            {
                int value = Convert.ToInt32(input[1]);
                queue.Enqueue(value);
            }
            else if (type == 2)
            {
                queue.Dequeue();
            }
            else if (type == 3)
            {
                Console.WriteLine(queue.Peek());
            }
        }
    }

    public class Queue
    {
        private Stack<int> s1 = new Stack<int>();
        private Stack<int> s2 = new Stack<int>();

        public void Enqueue(int x)
        {
            s1.Push(x);
        }

        public int Dequeue()
        {
            if (s2.Count == 0)
            {
                while (s1.Count > 0)
                {
                    s2.Push(s1.Pop());
                }
            }
            return s2.Pop();
        }

        public int Peek()
        {
            if (s2.Count == 0)
            {
                while (s1.Count > 0)
                {
                    s2.Push(s1.Pop());
                }
            }
            return s2.Peek();
        }
    }
}
