function gcd(a, b) {
    if(a % b === 0) {
        return b;
    } else {
        return gcd(b, a % b);
    }
}

function check(a, b) {
    var gcdA = gcd(a, b);

    if(gcdA === a) {
        return true;
    } else if(gcdA === 1) {
        return false;
    } else {
        a /= gcdA;
        gcdA = gcd(a, gcdA);
        return check(Math.max(a, gcdA), Math.min(a, gcdA));
    }
}

function solution(A, B) {
    var count = 0;
    for(var i=0; i<A.length; i++) {
        var bigNum = Math.max(A[i], B[i]);
        var smallNum = Math.min(A[i], B[i]);
        var div = gcd(bigNum, smallNum);

        if(bigNum === smallNum) {
            count++;
        } else if(check(bigNum, div) && check(smallNum, div)) {
            count++;
        }
    }

    return count;
}

console.log("solution", solution([15,10,3],[75,30,5]))