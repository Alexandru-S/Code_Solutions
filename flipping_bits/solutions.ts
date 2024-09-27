function flippingBits(n: number): number {
    const unasignedBits:number = n >>> 0;
    let flippedBits = ~unasignedBits >>> 0;  
    return flippedBits;
}