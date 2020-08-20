function solution(N) {
    var binaryArr = Array.from(N.toString(2), Number);
    var startPos = 0;
    var count = 0;
    var tracking = [];

    for(var i = 0 ; i < binaryArr.length; i++){
        if(binaryArr[i] === 1 && startPos === 1){
            tracking.push(count);
            count = 0;
        }
        else if(binaryArr[i] === 1 && startPos === 0){
            startPos = 1;
        }
        else if( binaryArr[i] ===  0 && startPos === 1){
            count++;
        }
    }
    tracking.sort();
    if(tracking.length){
        return tracking[tracking.length -1];
    }else{
        return 0;
    }
}