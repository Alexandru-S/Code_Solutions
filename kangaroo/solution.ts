function kangaroo(x1: number, v1: number, x2: number, v2: number): string {
    if (v1 == v2) 
    {
            return (x1 === x2) ? "YES" : "NO";
    }
    if ((x1 - x2) % (v2 - v1) === 0 && (x1 - x2) / (v2 - v1) >= 0) 
    {
            return "YES";
    }

    return "NO";


}