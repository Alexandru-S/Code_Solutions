function matchingStrings(strings: string[], queries: string[]): number[] {
    let result:number[] = new Array(queries.length).fill(0);
    
    for(let j = 0; j < queries.length; j++){
        for(let i  = 0 ; i < strings.length; i++){
            if(queries[j] === strings[i]){
                result[j] += 1
            }
        }
    }
    return result
}