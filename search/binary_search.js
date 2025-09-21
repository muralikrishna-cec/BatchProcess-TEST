// Binary Search function
function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) {
            return mid;  // Found
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Not found
}

// Example run
if (require.main === module) {
    let sorted = [11, 12, 22, 25, 34, 64, 90];
    let target = 25;
    let index = binarySearch(sorted, target);

    if (index !== -1) {
        console.log("Element", target, "found at index", index);
    } else {
        console.log("Element", target, "not found.");
    }
}

// Export for reuse
module.exports = binarySearch;
