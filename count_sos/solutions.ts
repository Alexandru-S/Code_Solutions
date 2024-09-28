function marsExploration(s: string): number {
    console.log(s)
    let count:number = 0;
    let countDifferences: number = 0;
    for(let i = 0 ; i < s.length ; i++){
        count = (count ===3) ? 0: count;
        if(count === 0 && s.charAt(i) !== 'S'){
                countDifferences++;
        }else if(count === 1 && s.charAt(i) !== 'O'){
                countDifferences++;   
        }else if(count === 2 && s.charAt(i) !== 'S'){
                countDifferences++;
        }
        count++;
    }
    return countDifferences
}