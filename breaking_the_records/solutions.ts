function breakingRecords(scores: number[]): number[] {
    let miniumumScore;
    let maximumScore;
    let records:[number,number] = [0,0]
    if(scores.length === 1){
        return records
    }
    for(let i = 0 ; i<scores.length;i++){
        if(i === 0){
            miniumumScore = scores[i]
            maximumScore = scores[i]
        }else{
            if(scores[i] < miniumumScore){
                records[1] +=1
                miniumumScore = scores[i]
            }
            if(scores[i] > maximumScore){
                records[0] +=1
                maximumScore = scores[i]
            }   
        }
    }
    return records
}