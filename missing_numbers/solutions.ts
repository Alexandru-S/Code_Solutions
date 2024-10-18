function missingNumbers(arr: number[], brr: number[]): number[] {
    const freqArr: { [key: number]: number } = {};
    const freqBrr: { [key: number]: number } = {};
    for (let num of arr) {
        freqArr[num] = (freqArr[num] || 0) + 1;
    }

    for (let num of brr) {
        freqBrr[num] = (freqBrr[num] || 0) + 1;
    }

    const missing: number[] = [];

    for (let num in freqBrr) {
        if (!freqArr[num] || freqArr[num] < freqBrr[num]) {
            missing.push(Number(num));
        }
    }

    return missing.sort((a, b) => a - b);
}