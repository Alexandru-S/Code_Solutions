
function solution(X, Y, D){
    no_of_jumps = Math.floor(Y / D);
    if(X + (D * no_of_jumps) < Y){
        no_of_jumps++;
    }
    return no_of_jumps;
}