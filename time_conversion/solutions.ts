function timeConversion(s: string): string {

    const timeSuffix = s.slice(-2)
    const hourTime = s.slice(0,2)
    console.log(s)
    console.log(hourTime)
    let newTime;
    if(timeSuffix === 'AM'){
        return s.slice(0,8)
    }else{
        
        if(hourTime === '12'){
            newTime = '00'
        }else{
            newTime = (parseInt(hourTime)+12).toString()
        }  
    }
    return newTime + s.slice(2, 8) 
    }