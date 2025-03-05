public static void staircase(int n)
{
    for(int i = 1 ;i <= n; i++){
        Console.Write(new string(' ', n-i));
        Console.WriteLine(new string('#',i));
    }
}