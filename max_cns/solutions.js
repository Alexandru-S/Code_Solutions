function solution(N, A){

    var lastMax = 0;
    var max = 0;
    var counters =  new Array (N).fill(0)

    for(var j=0; j < A.length; j++){
        if(A[j] < (N + 1)){
            var i = A[j] - 1;
            if (counters[i] < lastMax){
                counters[i] = lastMax;
            }
            counters[i]++;
            if (max < counters[i]){
                max = counters[i];
            }
        } else {
            lastMax = max;
        }
    }

    for(var j = 0; j < N; j++){
      if (counters[j] < lastMax){
        counters[j] = lastMax;
      }
    }
else

    return counters;

}
