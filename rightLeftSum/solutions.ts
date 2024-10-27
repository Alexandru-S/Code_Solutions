function balancedSums(arr: number[]): string {
    let totalSum:number = arr.reduce((acc,curr)=>acc+curr,0)
    let leftSum =0
    for(let i =0 ; i< arr.length; i++){
        let rightSum = totalSum - leftSum -arr[i]
        if(leftSum === rightSum){
            return "YES"
        }
        leftSum += arr[i]
    }
    return "NO"
}