function superDigit(n: string, k: number): number {
    let sum:number = 0;
    for (let char of n) {
      sum += Number(char);
    }
  
    sum *= k;
    if (sum <= 9) return sum;
    return superDigit(String(sum), 1);
  }