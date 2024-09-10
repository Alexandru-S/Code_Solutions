
function miniMaxSum(arr: number[]): void {
    // Write your code here
    const sortedArray = arr.sort((a,b)=>a-b)
    const minArray = sortedArray.slice(0,4)
    const maxArray = sortedArray.slice(-4)
    const minSum = sumArray(minArray)
    const maxSum = sumArray(maxArray)
    console.log(minSum,maxSum)

}

function sumArray(arr:number[]): number{
    return arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0)
}

