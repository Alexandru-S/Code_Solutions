function minimumNumber(n: number, password: string): number {
    const p:string = password; let faults:number = 0;
       if(!/[!@#$%^&*()+-]/.test(p)) faults++;
       if(!/[0-9]/.test(p)) faults++;
       if(p === p.toUpperCase()) faults++;
       if(p === p.toLowerCase()) faults++;
       if(n + faults < 6) faults += 6 - (faults + n);
       return faults 
   }