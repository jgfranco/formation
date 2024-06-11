function classify(adjList) {
  if (Object.keys(adjList).length === 0) return "BINARY TREE";

  let potentialRoots = new Set();
  let visited = new Set();
  let moreThanTwoChildren = false;
  let hasCycle = false;

  function dfs(node, parent) {
    visited.add(node);
    for (let child of adjList[node]) {
      if (child === parent) continue;
      if (visited.has(child)) {
        hasCycle = true;
      } else {
        dfs(child, node);
      }
    }
  }

  for (let k in adjList) {
    if (!visited.has(k)) {
      potentialRoots.add(k);
      dfs(k, null);
    }
    if (adjList[k].length > 2) {
      moreThanTwoChildren = true;
    }
  }

  if (hasCycle) {
    return "GRAPH";
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