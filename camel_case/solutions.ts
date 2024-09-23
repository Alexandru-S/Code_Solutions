function main() {
    // Enter your code here
    let finalResult:string = ''
    for(let line in inputLines){
        const readString:string =  inputLines[line]
        const readArray:string[] = readString.trim().split(';')
    
        if (readArray[0] === 'S') {
            let removeString: string = '';

            if (readArray[1] === 'M') {
                removeString = readArray[2].slice(0, -2);
            } else if (readArray[1] === 'C') {
                removeString = readArray[2].charAt(0).toLowerCase() + readArray[2].slice(1);
            } else {
                removeString = readArray[2];
            }
            const result = removeString.replace(/([A-Z])/g, ' $1').toLowerCase();
            finalResult += "\n" + result.trim();
        } 
        if (readArray[0] === 'C') {
            let addString: string[] = readArray[2].toLowerCase().split(' ');

            if (readArray[1] === 'M') {
                addString = addString.map((word, index) => index === 0 ? word : capitalize(word));
                finalResult += "\n" + addString.join('') + "()";
            } else if (readArray[1] === 'C') {
                addString = addString.map(word => capitalize(word));
                finalResult += "\n" + addString.join('');
            } else {
                addString = addString.map((word, index) => index === 0 ? word : capitalize(word));
                finalResult += "\n" + addString.join('');
            }
        }
    }
    console.log(finalResult.trimStart())
}
function capitalize(word: string): string {
    return word.charAt(0).toUpperCase() + word.slice(1);
}