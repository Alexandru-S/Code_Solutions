function gamingArray(arr: number[]): string {
    let moves = 0;
    let maxSofar = 0;
    for(let num of arr){
        if(num > maxSofar){
            maxSofar = num
            moves++;
        }
    }
    return moves % 2 === 0 ? "ANDY" : "BOB";
}