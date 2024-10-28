function misereNim(s: number[]): string {
    const allOnes = s.every(pile => pile === 1)
    let nimSum = 0;
    for(const pile of s){
        nimSum ^= pile;
    }
    if(allOnes){
        return s.length % 2 === 1? "Second" : "First";
    }else{
        return nimSum === 0 ? "Second" : "First";
    }
}