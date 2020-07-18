
console.log("solution", solution([-5,-3,-1,0,3,6]))

function solution(A){
    return [...new Set(A.map(s => Math.abs(s)))].length;
}