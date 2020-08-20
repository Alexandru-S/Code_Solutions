function solution(N) {
    var binary_arr = Array.from(N.toString(2), Number);
    var start_pos = 0;
    var count = 0;
    var tracking = [];

    for(var i = 0 ; i < binary_arr.length; i++){
        if(binary_arr[i] === 1 && start_pos === 1){
            tracking.push(count);
            count = 0;
        }
        else if(binary_arr[i] === 1 && start_pos === 0){
            start_pos = 1;
        }
        else if( binary_arr[i] ===  0 && start_pos === 1){
            count++;
        }
    }
    tracking.sort()
    if(tracking.length){
        return tracking[tracking.length -1];
    }else{
        return 0;
    }
}