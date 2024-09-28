function countingValleys(steps: number, path: string): number {
    let altitude:number = 0;
    let valleyCounter: number =0 ;
    const pathArray: string[] = path.split('');
    for(let i = 0; i < steps ; i++){
        console.log(pathArray[i]);
        if(pathArray[i] === 'U'){
            altitude++;
            if(altitude === 0){
                valleyCounter++;
            }
        }else{
            altitude--;
        }
    }
    return valleyCounter
}