function lonelyinteger(a: number[]): number {
    let n:number = a.length;
    let swapped:boolean;
    
    do{
        swapped = false;
        for(let i = 0 ; i < n-1 ; i++){
            if(a[i] > a[i+1]){
                [a[i],a[i+1]] = [a[i+1],a[i]]
                swapped=true
            }
        }
        n--;
        
    }while(swapped)

        for(let i = a.length - 1 ; i>0; i--){
            if(a[i] === a[i-1]){
                a.splice(i-1,2)
                i--;
            }
        }
    return a[0]
}