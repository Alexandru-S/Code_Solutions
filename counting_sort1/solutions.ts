function countingSort(arr: number[]): number[] {
    let result:number[] = new Array(arr.length).fill(0)
    for(let i = 0; i < arr.length ; i++){
        result[arr[i]] += 1
    }
    return result.slice(0,100)
}
