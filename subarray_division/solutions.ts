function birthday(s: number[], d: number, m: number): number {
    let segments:number = 0;
    for(let i = 0; i < s.length-m+1; i++){
        const segment:number[] = s.slice(i,i+m)
        const segmentSum:number = segment.reduce((prev, current) => prev + current + 0) 
        if(segmentSum === d){
            segments++;
        }
    }
    return segments;
}