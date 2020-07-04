function solution(A){
    // write your code in Javascript ecma 6

    var sum1 = A[0];
    var sum2 = 0;
    var P = 1;
    for (var i = P; i < A.length; i++) {
        sum2 += A[i];
    }
    var diff = Math.abs(sum1 - sum2);

    for (; P < A.length-1; P++) {
        sum1 += A[P];
        sum2 -= A[P];

        var newDiff = Math.abs(sum1 - sum2);
        if (newDiff < diff) {
            diff = newDiff;
        }
    }
    return diff;

}