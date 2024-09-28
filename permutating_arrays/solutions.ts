function twoArrays(k: number, A: number[], B: number[]): string {
    const sortedA:number[] = A.sort((a,b) => a-b);
    const sortedB:number[] = B.sort((a,b) => b-a);
    for(let i = 0 ; i < A.length ; i++){
        if(sortedA[i] + sortedB[i] < k ){
            return 'NO'
        }
    }
    return 'YES'
}