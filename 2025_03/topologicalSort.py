def to_adj_list(vertex_list, edge_list):
    output = {}
    for v in vertex_list:
        output[v] = []
    for frm, to in edge_list:
        output[frm].append(to)
    return output

def solution(vertex_list, edge_list):
    adj_list = to_adj_list(vertex_list, edge_list)
    visited = set()
    def dfs(curr_node):
        if curr_node in visited:
            return
        visited.add(curr_node)
        for neighbor in adjacency_list[curr_node]:
            dfs(neighbor)
    dfs(adj_list)




vertex_list = [
    "Prepare kitchen", "Mix flour", "Mix wet ingredients", "Combine", "Put in oven", "Clean kitchen"
]
edge_list = [
    ("Prepare kitchen", "Mix wet ingredients"),
    ("Prepare kitchen", "Mix flour"),
    ("Mix flour", "Combine"),
    ("Mix wet ingredients", "Combine"),
    ("Combine", "Put in oven"),
    ("Combine", "Clean kitchen"),
]

        Prepare Kitchen
            /     \
     Mix flour   Mix wet ingredients
              \ /
             Combine
              /     \
     Put in oven   Clean kitchen

Return a valid ordering such that all upstream steps come before all downstream steps. For example:

['Prepare kitchen', 'Mix flour', 'Mix wet ingredients', 'Combine', 'Clean kitchen', 'Put in oven']
OR
['Prepare kitchen', 'Mix wet ingredients', 'Mix flour', 'Combine', 'Clean kitchen', 'Put in oven']
OR
['Prepare kitchen', 'Mix wet ingredients', 'Mix flour', 'Combine', 'Put in oven', 'Clean kitchen']




  Prepare Kitchen      Dance
            /           |
     Mix flour   Mix wet ingredients
              \ /
             Combine
              /     \
     Put in oven   Clean kitchen
''' Start at any node that does not have a parent - source

'''

def get_sources(adj_list):
    possible_sources = set(adj_list.keys())
    for neighbors in adj_list.values():
        # if a node has an in-edge, then it can't
        # be a source
        for node in neighbors:
            if node in possible_sources:
                possible_sources.remove(node)
    return possible_sources

def brute_force(adj_list):
    sources = get_sources(adj_list)
    output = []
    while len(sources) > 0:
        output.extend(sources)
        for s in sources:
            del adj_list[s]
        sources = get_sources(adj_list)
    return output


def topo_sort(adjacency_list):
    stack = []
    visited = set()
    def dfs(curr_node):
        if curr_node in visited:
            return
        visited.add(curr_node)
        for neighbor in adjacency_list[curr_node]:
            dfs(neighbor)
        stack.append(curr_node)
    for node in adjacency_list.keys():
        if node not in visited:
            dfs(node)
    
    return list(reversed(stack))


    Map<indegrees, nodes>...