 public static int diagonalDifference(List<List<int>> arr)
    {
        int matrixLength = arr.Count;
        int leftDiag = 0;
        int rightDiag = 0;
        int leftCount = 0;
        int rightCount = matrixLength-1;
        for(int i = 0; i <matrixLength ;i++){
            for(int j = 0; j< matrixLength; j++){
                if(leftCount == j){
                    leftDiag += arr[i][j];
                    leftCount++;
                    break;
                }
            }
        }
       for(int i = 0; i <matrixLength ;i++){
            for(int j = 0; j< matrixLength; j++){
                if(rightCount == j){
                    rightDiag += arr[i][j];
                    rightCount--;
                    break;
                }
            }
        }
        
        if(rightDiag > leftDiag){
            return rightDiag -leftDiag;
        } else if (leftDiag > rightDiag){
            return leftDiag - rightDiag;
        }else{
            return 0;
        }

    }