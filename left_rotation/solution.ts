function rotateLeft(d: number, arr: number[]): number[] {
    const newLeft:number[]= arr.slice(0,d)
    const newRight: number[] = arr.slice(d,arr.length)
    return newRight.concat(newLeft)
}