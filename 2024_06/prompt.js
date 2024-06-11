function classify(adjList) {
  if (Object.keys(adjList).length === 0) return "BINARY TREE";

  let potentialRoots = new Set();
  let visited = new Set();
  let moreThanTwoChildren = false;

  for (let k in adjList) {
    k = parseInt(k)

    if (!visited.has(k)) {
      potentialRoots.add(k);
      visited.add(k);
    }
    if (adjList[k].length > 2) {
      moreThanTwoChildren = true;
    }

    for (let child of adjList[k]) {

      if (potentialRoots.has(child)) {
        potentialRoots.delete(child);
      }
      if (visited.has(child)) {
        return "GRAPH";
      }
      
      visited.add(child);
      
    }
  }

  if (potentialRoots.size === 1 && moreThanTwoChildren) {
    return "TREE";
  }
  if (potentialRoots.size === 1) {
    return "BINARY TREE";
  }

  return "GRAPH";
}

let multiTree = {
  1: [2, 3],
  2: [4],
  3: [5, 6, 7],
  4: []
};
console.log(classify(multiTree) === 'TREE');


let binaryTree = {
  1: [2, 3],
  2: [4],
  3: [],
  4: []
};
console.log(classify(binaryTree) === 'BINARY TREE');

let doubleRoot = {
  1: [2, 3],
  2: [4],
  3: [],
  4: [],
  5: []
};
console.log(classify(doubleRoot) === 'GRAPH');

let sharedParent = {
  1: [2, 3],
  2: [4],
  3: [4],
  4: []
};
console.log(classify(sharedParent) === 'GRAPH');

let oneNode = {
  1: []
};
console.log(classify(oneNode) === 'BINARY TREE');

let noNode = {};
console.log(classify(noNode) === 'BINARY TREE');

let oneNodeCycle = {
  1: [1]
};
console.log(classify(oneNodeCycle) === 'GRAPH');

let nestedCycle = {
  1: [2, 3],
  2: [],
  3: [3, 4],
  4: []
};
console.log(classify(nestedCycle) === 'GRAPH');
