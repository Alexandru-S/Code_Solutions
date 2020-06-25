function solution(N) {
    var binary = Array.from(N.toString(2), Number);
    var start = 0
    var count = 0
    var tracking = []

    for(var i = 0 ; i < binary.length; i++){
        if(binary[i] === 1 && start === 1){
            tracking.push(count)
            count = 0
        }
        else if(binary[i] === 1 && start === 0){
            start = 1;
        }
        else if( binary[i] ===  0 && start === 1){
            count++
        }
    }
    tracking.sort()
    if(tracking.length){
        return tracking[tracking.length -1]
    }else{
        return 0;
    }
}