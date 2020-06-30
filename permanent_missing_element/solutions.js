function solution(A){
    A.sort()
    for(var i = 0; i< A.length; i++){
        if(A[i]+1 !== A[i+1]){
            return A[i]+1
        }
    }
}