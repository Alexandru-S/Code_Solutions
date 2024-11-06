function sumXor(n: number): number {
    if(n===0){
        return 1
    }
    const binaryString:string = n.toString(2)
    let zeroCount:number = 0;
    for(let i=0; i<binaryString.length; i++){
        if(binaryString[i] === "0"){
            zeroCount++
        }
    }
    return Math.pow(2,zeroCount)
}