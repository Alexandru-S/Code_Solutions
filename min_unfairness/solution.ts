function maxMin(k: number, arr: number[]): number {
    arr.sort((a,b)=>a-b)
    let minUnfairness = Infinity;
     for (let i = 0; i <= arr.length - k; i++) {
        const currentUnfairness = arr[i + k - 1] - arr[i];
        minUnfairness = Math.min(minUnfairness, currentUnfairness);
    }
    return minUnfairness;

}