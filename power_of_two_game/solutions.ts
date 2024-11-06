function counterGame(n: number): string {
    if(n ===1){
        return "Richard"
    }
    let count:number = 0
    let z:number = Math.log2(n)
    console.log(n)
    console.log(z)
    while(n > 1) {
        if(Number.isInteger(z)) {
            n = n/2
            count++ 
       } else {
           n = n - 2**(Math.floor(z))
           z = Math.log2(n)
           count++ 
       }
    }
    if(count % 2 ===0){
        return "Richard"
    }else{
        return "Louise"
    }

}