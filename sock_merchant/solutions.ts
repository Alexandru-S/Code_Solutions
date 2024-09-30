function sockMerchant(n: number, ar: number[]): number {
    let swapped: boolean;
       do {
           swapped = false;
           for (let i = 0; i < n - 1; i++) {
               if (ar[i] > ar[i + 1]) {
                   [ar[i], ar[i + 1]] = [ar[i + 1], ar[i]];
                   swapped = true;
               }
           }
           n--; 
       } while (swapped);
   
       let count = 0;
       for (let i = ar.length - 1; i > 0; i--) {
           if (ar[i] === ar[i - 1]) {
               count++; 
               ar.splice(i - 1, 2); 
               i--; 
           }
       }
        return count;
   }