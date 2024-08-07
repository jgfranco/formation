'''

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


    [Put in oven, clean kitchen, combine, Mix flour, Mix wet ingredients, Prepare Kitchen]

    reverse the above list to get the answer



# arrange all the nodes in increasing order of indegree (kahn's algorithm)

Return a valid ordering such that all upstream steps come before all downstream steps. For example:

['Prepare kitchen', 'Mix flour', 'Mix wet ingredients', 'Combine', 'Clean kitchen', 'Put in oven']
OR
['Prepare kitchen', 'Mix wet ingredients', 'Mix flour', 'Combine', 'Clean kitchen', 'Put in oven']
OR
['Prepare kitchen', 'Mix wet ingredients', 'Mix flour', 'Combine', 'Put in oven', 'Clean kitchen']

'''

def to_adj_list(vertex_list, edge_list):
    output = {}
    for v in vertex_list:
        output[v] = []
    for frm, to in edge_list:
        output[frm].append(to)
    return output

def solution(src_node, adj_list, visited, result):
    
    def dfs(curr_node):
        if curr_node in visited:
            return
        visited.add(curr_node)

        for neighbor in adj_list[curr_node]:
            dfs(neighbor)

        result.append(curr_node)

    dfs(src_node)
   
    return


vertex_list = [
    "Put in oven", "Prepare kitchen", "Mix flour", "Mix wet ingredients", "Combine", "Clean kitchen"
]

edge_list = [
    ("Prepare kitchen", "Mix wet ingredients"),
    ("Prepare kitchen", "Mix flour"),
    ("Mix flour", "Combine"),
    ("Mix wet ingredients", "Combine"),
    ("Combine", "Put in oven"),
    ("Combine", "Clean kitchen"),
]


def topological_sorting(edge_list, vertex_list):
    adj_list = to_adj_list(vertex_list, edge_list)
    visited = set()
    result = []


    for vertex in vertex_list:
        if vertex not in visited:
            solution(vertex, adj_list, visited, result)

    result.reverse()
    return result

print(topological_sorting(edge_list, vertex_list))

# https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/