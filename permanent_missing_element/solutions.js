function solution(A) {
    if(!A.length){
        return 1;
    }
    A.sort(function(a,b){return a-b});
    if(A[0] !== 1){
        return 1;
    };
    for(var i = 0; i < A.length; i++){
        if(A[i]+1 !== A[i+1]){
            return A[i] + 1;
        }
    }
    return A[A.length-1] +1;
}
