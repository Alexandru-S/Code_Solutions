//For a number to be power of two it has to be greater than and AND with itself -1 to 0
public static bool isPowerOfTwo(long n){
    return n>0 && (n & (n-1)) ==0;
}
// To find the closest power of two just *2 until just befpore youre about to pass the number
public static long highestPowerOfTwoLessThan(long n){
    long p = 1;
    while(p*2 < n){
        p*=2;
    }
    return p;
}

public static string counterGame(long n)
{
    int count = 0;
    if(n == 1){
        return "Richard";
    }
    while(n>1){
        if(isPowerOfTwo(n)){
            n = n/2;   
        }else{
            n-=highestPowerOfTwoLessThan(n);
        }
         count ++;
    }
    return (count %2 ==0)? "Richard":"Louise";
}
