'''
Install dependencies in order

A popular software project has recently published a new version, and you have been tasked with installing the required dependencies. However, the dependencies themselves have their own dependencies which must be installed in a certain order. To help simplify this, you've decided to create a system that organizes the installation process.

You are given a list of n software dependencies, where each dependency i has a unique identifier from 0 to n - 1. You are also given a list of pairs where pairs[i] = [a, b] indicates that software b must be installed before software a can be installed.

Write a function install_order(n: int, dependencies: List[List[int]]) -> List[int] that returns the order that the software should be installed to satisfy all dependencies. If there are multiple orders, return any of them. If there is no valid installation order, return an empty list.
 

[
  3: [2,0]
  2: [0,1]
]

0,1,2,3

 2: [3]
 0: [3, 2]
 1: [2]


EXAMPLE(S)
n = 4
dependencies = [[3, 2], [3, 0], [2, 0], [2, 1]]
order = [0, 1, 2, 3]


{
  3 : [0,2]
  2 : [0,1]
  4 : [5]
  1 : [5]
}

potentialRoots = [0] (set)
{
  3: [2, 0],
  2: []
   
}
[0,5,1,2,3,4]


n = 6
dependencies = [[3, 2], [3, 0], [2, 0], [2, 1], [4, 5], [1, 5]]
order = [5, 4, 0, 1, 2, 3] or [5, 0, 1, 2, 3, 4] (multiple answers)
 
[
  3: [2,0]
  2: [0,1]
]

{
  3: [2,0]

}



[0,1]
[
  3: [2,0,4] 
  2: [0,1]
  6 : [0]
]


approach_1 post order dfs
  0. init dictionary to store requirements 
  1. init installed_software as set of numbers range from 0-n {0,1,2,3...}

# populate dictonary and remove from install_softwares
  2. iterate depenedencies array 
    3. if first element in array is in dependency 
      if key doesn't exisit:
        add element as key and value is array of second element array[0] : [array[1]]  
      else 
        add 2nd element to requreiments[array[0]] value 
      
      4. remove element from installed_softwares
[0,1,2,6]
[
  3: [2,0] 
  2: [0,1]
  6 : [0]
]
  # 
    5. loop through requirements dictionary and call dfs when needed
        
        6.if current key is not installed/ in installed_software
            is_possible = canInstall()
            if is_possible is false - return empty array
            add current key to install_software
    7. return install_software

  function canInstall (dictioanry,software_to_install,installed_software,path) recursive helper -> boolean,path
    # adds current software to install if possible otherwise return false
    1. access requirements
    2. loop through requirements and see if they are in installed_software
      3. if not in installed_software, call dfs on that requirement
          is_possible = dfs()
          if is_possible is false - return False
          add to installed_softwares
    return true
  

FUNCTION SIGNATURE
def install_order(n: int, dependencies: List[List[int]]) -> List[int]:
'''

def install_order(n, dependencies):

  installedSoftware = set()
  dependenciesMap = {}
  for a,b in dependencies:
    dependenciesMap[a] = dependenciesMap.get(a, []).append(b)
  
  print(dependenciesMap)


print(install_order(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))