function classify(adjList) {
  if (Object.keys(adjList).length === 0) return "BINARY TREE";

  let potentialRoots = new Set();
  let visited = new Set();
  let moreThanTwoChildren = false;

  for (let k in adjList) {
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
      } else {
        visited.add(child);
      }
    }
  }

  // Check if all nodes have a parent
  for (let k in adjList) {
    if (!visited.has(k)) {
      return "GRAPH";
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
console.log(classify(multiTree) , 'TREE');