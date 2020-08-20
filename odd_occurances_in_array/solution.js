
function solution(A) {
    var N = A;
    N.sort(function(a,b){return b-a});
    for(var i = 0 ; i < N.length; i++){
        if(N[i+1] === undefined){
            return parseInt(N.join(''), 10);
        }
        if(N[i] === N[i+1]){
            N.splice(i,2);
            i=-1;
        }
    }
}
