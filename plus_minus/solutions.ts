'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

function plusMinus(arr: number[]): void {
    const positiveIntegers = arr.filter(item => Number.isInteger(item) && item > 0)
    const negativeIntegers = arr.filter(item => Number.isInteger(item) && item < 0)
    const zeroIntegers = arr.filter(item => Number.isInteger(item) && item === 0)
    console.log(positiveIntegers.length/arr.length)
    console.log(negativeIntegers.length/arr.length)
    console.log(zeroIntegers.length/arr.length)

}

function main() {
    const n: number = parseInt(readLine().trim(), 10);

    const arr: number[] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
