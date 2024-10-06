function pickingNumbers(a: number[]): number {
    let compareArray: Record<number,number> = {}
    for (let num of a){
        if(compareArray[num]){
            compareArray[num]++
        }else{
            compareArray[num] = 1
        }
    }
    let maxSub: number = 0;
    for(let numId in compareArray){
        let currentNum = parseInt(numId)
        let currentCount: number = compareArray[currentNum];
        if(compareArray[currentNum+1]){
            currentCount += compareArray[currentNum+1]
        }
        if(currentCount > maxSub){
            maxSub = currentCount;
        }
    }
return maxSub
}