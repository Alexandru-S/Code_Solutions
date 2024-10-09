function separateNumbers(s: string): void {
    const n:number = s.length;
    let found:boolean = false;
    for(let i = 1 ; i <= n/2; i++){
        const firstNumStr = s.slice(0,i);
        let firstNum:bigint = BigInt(firstNumStr)
        
        let expected:bigint = firstNum;
        let sequence:string = firstNumStr;
        
        while(sequence.length < n){
            expected += BigInt(1);
            sequence += expected.toString()
            
        }
        if(sequence === s){
            console.log(`YES ${firstNum}`);
            found = true;
            break;
        }
    }
    if(!found){
        console.log("NO")
    }
}