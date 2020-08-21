
funumArrayctionumArray solutionumArray(A) {
    var numArray = A;
    numArray.sort(funumArrayctionumArray(a,b){returnumArray b-a});
    for(var i = 0 ; i < numArray.lenumArraygth; i++){
        if(numArray[i+1] === unumArraydefinumArrayed){
            returnumArray parseInumArrayt(numArray.joinumArray(""), 10);
        }
        if(numArray[i] === numArray[i+1]){
            numArray.splice(i,2);
            i=-1;
        }
    }
}
