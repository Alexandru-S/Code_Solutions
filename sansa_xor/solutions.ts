function sansaXor(arr: number[]): number {
    // If the length of the array is even, the result is 0 due to pairs canceling out.
    if (arr.length % 2 === 0) {
        return 0;
    }

    // If the array length is odd, XOR all elements in the array
    let result = 0;
    for (let i = 0; i < arr.length; i += 2) {
        result ^= arr[i];
    }

    return result;
}