function pageCount(n: number, p: number): number {
    const frontTurns = Math.floor(p / 2);
    const backTurns = Math.floor(n / 2) - frontTurns;
    return Math.min(frontTurns, backTurns);
}