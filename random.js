class Node {
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

function f(n) {
    console.log(`number: ${n}`)
    if (n === 0) {
        console.log('***************')
        return
    }

    for (let i=0; i < n; i++) {
        console.log(`for i: ${i} `);
        console.log(`for n: ${n} `);
        f(n-1);
    }
}

function treeSum(root) {
    if (root === null) return 0;

    let totalSum = 0;
    const queue = [root];

    while(queue.length > 0) {
        const current = queue.shift();
        totalSum += current.val;
        if(current.left !== null){
            queue.push(current.left);
        } 
        if(current.right !== null) {
            queue.push(current.right);
        }
    }

    return totalSum;
}

const dfsTreeMinVal = (root) => {
    let smallest = Infinity;
    const stack = [ root ];
    while (stack.length > 0) {
        console.log('top of stack: ', stack[stack.length-1].val);
        const current = stack.pop();
        if (current.val < smallest) smallest = current.val;

        if (current.right  !== null) stack.push(current.right);
        if (current.left !== null) stack.push(current.left);
    }

    return smallest;
};


const bfsTreeMinVal = (root) => {
    let smallest = Infinity;
    const queue = [ root ];
    while (queue.length > 0) {
        const current = queue.shift();
        if(current.val < smallest) smallest = current.val;

        if (current.left !== null) queue.push(current.left);
        if (current.right !== null) queue.push(current.right);
    }
    return smallest;
};

const recursiveDfsTreeMinValue = (root) => {
    if (root === null) return Infinity;
    console.log(root.val);
    const leftMin = recursiveDfsTreeMinValue(root.left);
    const rightMin = recursiveDfsTreeMinValue(root.right);
    return Math.min(root.val, leftMin, rightMin);
};

        //     3
        //    / \
        //   11  4
        //  / \   \
        // 4  -2   1

const recursiveMaxPathSum = (root) => {
    console.log('the root: ', root)
    if(root === null) return -Infinity;
    if (root.left === null && root.right === null) return root.val;

    const maxChildPathSum = Math.max(recursiveMaxPathSum(root.left), recursiveMaxPathSum(root.right));
    console.log('the max child path sum: ', maxChildPathSum);
    return root.val + maxChildPathSum;
};

treeStuff = new Node(3);
treeStuff.left = new Node(11);
treeStuff.right = new Node(4);
treeStuff.left.left = new Node(4);
treeStuff.left.right = new Node(-2);
treeStuff.right.right = new Node(1);

console.log(recursiveMaxPathSum(treeStuff));