public static long sumXor(long n)
{
  // Special case if n=0 then n+x == x AND n^x ==x
  if(n == 0){
      return 1;
  }
  // Declare count
  int zeroBits = 0;
  // loop through each bit of n, shifting right until n == 0
  while(n > 0){
      // Special case, check the first bit ANDs with 1 like 1001 & 0001 = 0001 but 1000 & 0001 = 0000 
     // In this special case it means that because LeastSignificantBit is 0 it can be a 0 or 1 when adding later on, and wont cause a carry (see binary addition)
      if((n&1) == 0 ){
          zeroBits++;
      }
      // shift to the right by 1 bit
      n >>=1;
  }
  // 1L declares a long with value 1 so 0001
  // << X is a way with dealing with powers of 2
  // << 3 means 2^3 = 8 or  1000
  return 1L<< zeroBits;
}
