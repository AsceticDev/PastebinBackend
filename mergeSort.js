function mergeSort(arr) {
    if (arr.length < 2) {
        return arr;
    }

    arrLen = (arr.length);

    const middleIndex = Math.floor(arrLen / 2);
    const leftArr = arr.slice(0, middleIndex);
    const rightArr = arr.slice(middleIndex, arrLen);

    console.log('\nnew mergeSort');
    console.log(arr);
    console.log('left Array: ', leftArr);
    console.log('right Array: ', rightArr);

    return merge(mergeSort(leftArr), mergeSort(rightArr));
}


function merge(leftArr, rightArr) {
    console.log('\n');
    console.log(`In Merge \nleft array: ${leftArr}\nright array: ${rightArr}`);
    let resultArr = []
    let leftIndex = 0
    let rightIndex = 0

    while(leftIndex < leftArr.length && rightIndex < rightArr.length) {
        if (leftArr[leftIndex] < rightArr[rightIndex]) {
            resultArr.push(leftArr[leftIndex]);
            console.log('pushing: ', leftArr[leftIndex]);
            leftIndex += 1;
        }else{
            resultArr.push(rightArr[rightIndex]); 
            console.log('pushing: ', rightArr[rightIndex]); 
            rightIndex += 1;
        }
    }

    console.log(`leftarr slice: ${leftArr.slice(leftIndex)}`)
    console.log(`rightarr slice: ${rightArr.slice(rightIndex)}`)
    console.log('resultarr before concat: ', resultArr)
    return resultArr.concat(leftArr.slice(leftIndex)).concat(rightArr.slice(rightIndex));
}


let arr = [12, 3, 16, 6, 5, 1];


console.log(mergeSort(arr));
