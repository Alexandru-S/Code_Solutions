function diagonalDifference(arr: number[][]): number {
    let leftIncrement = 0;
    let rightIncrement = arr[0].length -1;
    let leftDiagonal = 0;
    let rightDiagonal = 0;
    for(let i = 0; i < arr.length; i ++){
        for (let j = 0; j < arr[i].length; j++){
            if(j === leftIncrement && leftIncrement === i){
                leftDiagonal += arr[i][j];
                leftIncrement += 1;
            }
            if(j === rightIncrement){
                rightDiagonal += arr[i][j]
                rightIncrement -= 1;
            }
        }
    }
    if(rightDiagonal > leftDiagonal){
        return rightDiagonal - leftDiagonal
    }else if (rightDiagonal < leftDiagonal){
        return leftDiagonal - rightDiagonal
    }else{
        return 0
    }
}