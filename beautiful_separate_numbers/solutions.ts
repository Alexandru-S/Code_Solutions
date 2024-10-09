function separateNumbers(s: string): void {
    const n = s.length;
    let found = false;

    // Start by trying different lengths for the first number in the sequence
    for (let i = 1; i <= n / 2; i++) {
        // Take the first i digits as the starting number
        const firstNumStr = s.slice(0, i);
        let firstNum = BigInt(firstNumStr);
        
        let expected = firstNum;
        let sequence = firstNumStr;

        // Build the expected sequence
        while (sequence.length < n) {
            expected += BigInt(1);
            sequence += expected.toString();
        }

        // If the sequence matches the original string, it is beautiful
        if (sequence === s) {
            console.log(`YES ${firstNum}`);
            found = true;
            break;
        }
    }

    if (!found) {
        console.log("NO");
    }

}