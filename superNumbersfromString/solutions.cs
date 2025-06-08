// To get super digit its faster to sum and multiply by k first time
public static long superDigit(string n, int k)
{
    long sum = 0;
    foreach(var charn in n){
        sum += long.Parse(charn.ToString());
    }
    sum *=k;
    if(sum<10){
        return sum;
    } else{
        return superDigit(sum.ToString(),1);
    };

}
