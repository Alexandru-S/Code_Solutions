function gridChallenge(grid: string[]): string {
    const cLength:number = grid.length
    let newGrid:string[] = new Array(cLength)
    for(let i = 0; i<cLength;i++){
        newGrid[i] = grid[i].split('').sort().join('');
        
    }
    const rLength = newGrid[0].length
    for(let i = 0 ; i < rLength; i++){
        let checkArray:string = ''
        for(let j = 0; j < cLength; j++){
            checkArray += newGrid[j].charAt(i)
        }
        const trueSort = checkArray.split('').sort().join('');
        if(trueSort !== checkArray){
            return "NO"
        }
    }
    return "YES"
}