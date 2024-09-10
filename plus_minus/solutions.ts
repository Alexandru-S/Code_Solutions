
function plusMinus(arr: number[]): void {
    const positiveIntegers = arr.filter(item => Number.isInteger(item) && item > 0)
    const negativeIntegers = arr.filter(item => Number.isInteger(item) && item < 0)
    const zeroIntegers = arr.filter(item => Number.isInteger(item) && item === 0)
    console.log(positiveIntegers.length/arr.length)
    console.log(negativeIntegers.length/arr.length)
    console.log(zeroIntegers.length/arr.length)

}