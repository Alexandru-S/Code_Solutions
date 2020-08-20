function solution(A, K){
    K = K > A.length ? K%A.length : K;
    A.unshift.apply(A, A.splice(A.length - K, K));
    return A;
}