function pangrams(s: string): string {
    const alphabet:string = 'abcdefghijklmnopqrstuvwxyz';
    const lowerCaseString: string =s.toLocaleLowerCase();
    for(let letter of alphabet){
        if(!lowerCaseString.includes(letter)){
            return 'not pangram';
        }
    }
    return 'pangram';
}