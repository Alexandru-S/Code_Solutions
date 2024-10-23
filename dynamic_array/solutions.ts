function dynamicArray(n: number, queries: number[][]): number[] {
    let emptyArrays: number[][] = new Array(n).fill(null).map(() => []);
    let lastAnswer = 0;
    let results: number[] = []
    
    // Process each query
    for (let query of queries) {
        let queryType = query[0];
        let x = query[1];
        let y = query[2];

        // Compute the index using (x ^ lastAnswer) % n
        let idx = (x ^ lastAnswer) % n;

        if (queryType === 1) {
            // Type 1 query: Append y to emptyArrays[idx]
            emptyArrays[idx].push(y);
        } else if (queryType === 2) {
            // Type 2 query: Find the element at position y % size(emptyArrays[idx])
            let size = emptyArrays[idx].length;
            lastAnswer = emptyArrays[idx][y % size]; // Update lastAnswer
            results.push(lastAnswer); // Store lastAnswer in results
        }
    }
    // Return the results array containing all lastAnswer values from type 2 queries
    return results;
}