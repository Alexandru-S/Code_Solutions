function caesarCipher(s: string, k: number): string {
    const alphabet: string = "abcdefghijklmnopqrstuvwxyz";
    const alphabetUpper: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    k = k % 26;
    let newLeft: string = alphabet.slice(k) + alphabet.slice(0, k);
    let newLeftUpper: string = alphabetUpper.slice(k) + alphabetUpper.slice(0, k);
  
    let resultString: string = "";
    for (let letter of s) {
        if (alphabet.includes(letter)) {
            let oldCoord = alphabet.indexOf(letter);
            resultString += newLeft.charAt(oldCoord);
        } else if (alphabetUpper.includes(letter)) {
            let oldCoord = alphabetUpper.indexOf(letter);
            resultString += newLeftUpper.charAt(oldCoord);
        } else {
            resultString += letter;
        }
    }
    return resultString;
}