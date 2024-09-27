function flippingBits(n: number): number {
    const unasignedBits:number = n >>> 0; // convert to 32 unasigned bitwise
    let flippedBits = ~unasignedBits >>> 0;  //flip with NOT ~ and convert back to number
    return flippedBits;
}