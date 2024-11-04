function formingMagicSquare(s: number[][]): number {
    const expectedResult = 15;

    // Helper function to generate all permutations of an array
    function permute(arr: number[]): number[][] {
        if (arr.length === 1) return [arr];
        const permutations: number[][] = [];
        for (let i = 0; i < arr.length; i++) {
            const rest = permute(arr.slice(0, i).concat(arr.slice(i + 1)));
            for (const perm of rest) {
                permutations.push([arr[i], ...perm]);
            }
        }
        return permutations;
    }

    // Helper function to check if a 1D array represents a magic square when viewed as a 3x3 grid
    function isMagicSquare(square: number[]): boolean {
        return (
            square[0] + square[1] + square[2] === expectedResult && // Row 1
            square[3] + square[4] + square[5] === expectedResult && // Row 2
            square[6] + square[7] + square[8] === expectedResult && // Row 3
            square[0] + square[3] + square[6] === expectedResult && // Column 1
            square[1] + square[4] + square[7] === expectedResult && // Column 2
            square[2] + square[5] + square[8] === expectedResult && // Column 3
            square[0] + square[4] + square[8] === expectedResult && // Diagonal 1
            square[2] + square[4] + square[6] === expectedResult    // Diagonal 2
        );
    }

    // Generate all valid 3x3 magic squares
    function generateMagicSquares(): number[][][] {
        const allPermutations = permute([1, 2, 3, 4, 5, 6, 7, 8, 9]);
        const magicSquares: number[][][] = [];

        for (const perm of allPermutations) {
            if (isMagicSquare(perm)) {
                magicSquares.push([
                    [perm[0], perm[1], perm[2]],
                    [perm[3], perm[4], perm[5]],
                    [perm[6], perm[7], perm[8]],
                ]);
            }
        }
        return magicSquares;
    }

    // Generate magic squares dynamically
    const magicSquares = generateMagicSquares();

    // Calculate the minimum cost to convert s to a magic square
    let minCost = Infinity;

    for (const magic of magicSquares) {
        let cost = 0;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                cost += Math.abs(s[i][j] - magic[i][j]);
            }
        }
        minCost = Math.min(minCost, cost);
    }

    return minCost;
}
