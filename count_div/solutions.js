function solution(A, B ,K){
    var array = Array.from(new Array(B-A), (x,i) => i+A)
    var count = 0;
    for(var i in array){
        if(i%2 === 0){
            count++
        }
    }
    return count
}