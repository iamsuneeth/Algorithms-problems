/**
 * 
 * @param {* depth of current tree} depth 
 * @param {* index of current node} index 
 * @param {* is max user or not} isMax 
 * @param {* array of final states} scores 
 * @param {* maximum depth of the tree} maxDepth 
 */
const miniMax = (depth, index, isMax, scores, maxDepth) => {

    if (depth === maxDepth)
        return scores[index];
    if (isMax) {
        return Math.max(
            miniMax(depth + 1, 2 * index, false, scores, maxDepth),
            miniMax(depth + 1, 2 * index + 1, false, scores, maxDepth)
        )
    } else {
        return Math.min(
            miniMax(depth + 1, 2 * index, true, scores, maxDepth),
            miniMax(depth + 1, 2 * index + 1, true, scores, maxDepth)
        )
    }
}

/**
 * 
 * @param {* number} n 
 */
const log2 = n => (
    (n === 1) ? 0 : 1 + log2(n / 2)
)

/**
 * test function
 */
const test = () => {
    const scores = [3, 5, 2, 9, 12, 5, 23, 23];
    const height = log2(scores.length);
    console.log("best state: ", miniMax(0, 0, true, scores, height));
}

test();
