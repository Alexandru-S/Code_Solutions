
function countSort(arr: string[][]): void {
    // Create a counting array with 100 buckets (since the range of indices is 0 to 99)
    const countingArr: string[][] = Array.from(Array(100), () => []);

    let middle = Math.floor(arr.length / 2); // Calculate the midpoint to replace the first half with '-'

    // Process each element in the array
    for (const [indexStr, str] of arr) {
        const index = parseInt(indexStr); // Convert the string index to a number

        if (middle > 0) {
            // Replace with '-' for the first half of the elements
            countingArr[index].push('-');
            middle -= 1;
        } else {
            // Push the original string for the second half
            countingArr[index].push(str);
        }
    }

    // Flatten the counting array and join the strings with a space
    console.log(countingArr.flat().join(' '));
}