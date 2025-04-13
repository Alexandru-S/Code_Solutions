 public static List<int> gradingStudents(List<int> grades)
    {
        List<int> result = Enumerable.Repeat(0, grades.Count).ToList();
        for(int i = 0; i < grades.Count; i++){
            if(grades[i]<38){
                result[i] = grades[i];
                continue;
            }else{
                if(grades[i] % 5 ==0 || grades[i] % 5 <3 ){
                    result[i] = grades[i];
                }else{
                    result[i] = grades[i] + (5 - grades[i]%5);
                }
            }
        
        }
        return result;
    }
