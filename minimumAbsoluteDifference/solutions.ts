function minimumAbsoluteDifference(arr: number[]): number {
    let minimumDifference:number=Infinity;
    arr.sort((a,b)=>a-b)
    for(let i = 0; i < arr.length-1; i++){
        const localDifference = Math.abs(arr[i]-arr[i+1])
        if(localDifference < minimumDifference){
            minimumDifference = localDifference;
        }
    }
    return minimumDifference
}