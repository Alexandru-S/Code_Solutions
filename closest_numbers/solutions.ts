function closestNumbers(arr: number[]): number[] {
    arr.sort((a,b) => a-b)
    let smallestDifference:number = Infinity;
    for(let i = 0 ; i < arr.length - 1; i++){
        let currentDifference:number = Math.abs(arr[i]-arr[i+1]);
        if(currentDifference<smallestDifference){
            smallestDifference = currentDifference;
        }
    }
    let resultArray:number[] = new Array();
    for(let i = 0; i<arr.length -1; i++){
        if(Math.abs(arr[i] -arr[i+1]) === smallestDifference){
            resultArray.push(arr[i])
            resultArray.push(arr[i+1])
        }
    }
    
    return resultArray

}