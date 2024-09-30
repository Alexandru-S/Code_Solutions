function migratoryBirds(arr: number[]): number {
    const birdCounting:Record<number,number> = {}
    for(let bird of arr){
        if(birdCounting[bird]){
            birdCounting[bird]++;
        }else{
            birdCounting[bird] = 1;
        }
    }
    let maxCount: number = 0;
    let mostFrequentBird = Infinity;
    for(let birdId in birdCounting){
        const count = birdCounting[birdId]
        const numericBirdId = parseInt(birdId)
         if (count > maxCount || (count === maxCount && numericBirdId < mostFrequentBird)) {
            maxCount = count;
            mostFrequentBird = numericBirdId;
        }
    }
    return mostFrequentBird;
}