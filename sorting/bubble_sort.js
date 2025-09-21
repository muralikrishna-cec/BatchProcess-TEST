// Bubble Sort function
function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

// Example run
if (require.main === module) {
    let numbers = [64, 34, 25, 12, 22, 11, 90];
    console.log("Original Array:", numbers);
    console.log("Sorted Array:", bubbleSort(numbers));
}

// Export for reuse
module.exports = bubbleSort;
