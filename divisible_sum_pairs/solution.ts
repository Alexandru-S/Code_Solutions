function divisibleSumPairs(n: number, k: number, ar: number[]): number {
    let countMatches : number = 0;
    for (let i = 0 ; i< n ; i++){
        for ( let j = i+1 ; j < n ; j ++){
            const result:number = ar[i] + ar[j]
            if(result % k === 0){
              countMatches++;   
            }
        }
    }
    return countMatches
}