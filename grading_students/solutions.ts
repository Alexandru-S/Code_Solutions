function gradingStudents(grades: number[]): number[] {
    for(let i = 0 ; i < grades.length ; i++){
        if(grades[i] > 37){
            if((Math.floor(grades[i]/5) + 1) * 5 - grades[i] < 3){
                grades[i] = (Math.floor(grades[i]/5) + 1) * 5
            }
        }
    }
    return grades
}