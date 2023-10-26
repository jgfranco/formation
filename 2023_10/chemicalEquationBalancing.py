'''
❓ PROMPT
Check whether the string s is a balanced chemical equation. 
The equation represents a chemical reaction that changes matter 
from one form to another, and since matter cannot be destroyed, 
valid equations must be balanced. Matter is made of molecules, 
and molecules are made of atoms. A balanced equation means 
that both sides have the same number of every atom.

An atom is a string that starts with an uppercase English letter 
followed by some or no lowercase English letters. For example, 
"A" and "Abc" are 1 atom each, but "FG" is 2 atoms, "F" and "G", 
and "hello" is invalid.  A molecule is one or more atoms.

The chemical equation is a string in the following format: 
molecule (+ molecule)* = molecule (+ molecule)*, where " * " 
means it repeats 0+ times. For example, "A = B", "A = B + C", 
and "A + B + C = D + E + F" are chemical equations but "X + Y = ", 
"X = + Z" are not.

A molecule is a concatenation of an optional molecule coefficient 
and a string representing the concatenation of the atoms with each 
of their optional atom coefficients. The coefficient is a positive 
integer less than 1000 that indicates how many times the molecule 
or atom appears in the equation. For example, "Cu12" means there are 
12 "Cu" atoms. "3H2O" means there are 6 "H" atoms and 3 "O" atoms 
because 3 is the coefficient of the "H2O" molecule, and 2 is the 
coefficient of the "H" atom. The coefficient of the "O" atoms is 
absent, meaning there's only 1 of that atom per molecule.

Example(s)
                                       
For s = "2H2 + O2 = 2H2O", the output is True.
Left side: 4 * "H" and "2 * O"
Right side: 4 * "H" and "2 * O"

For s = "1000H2O = Au + Ag", the output is False.
Left side: 2000 * "H" and "1000 * O"
Right side: 1 * "Ag" and "1 * Au"
 

🔎 EXPLORE
List your assumptions & discoveries:

use a dictionary to store the atom count 

- split the string at the "=" sign, we are left with a left and right side if the equation is properly structured  
- split both left side and right side at the "+" sign to get left side molecules and right side molecules
- parse the molecule, traverse the string
  - ininitialize the coefficient it at 1, and update it if exists in the molecule
  - 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
is_balanced(s: str) -> bool:
'''

def getCoefficient(molecule):
  p = 0
  coefficient = ""
  while molecule[p].isdigit():
    coefficient +=  molecule[p]
    p +=1

  if coefficient =="": return 1

  return int(coefficient)
    
def getAtoms(molecule, coefficient, atoms):
  p = 0
  if coefficient != 1:
    p = len(str(coefficient))

  while p < len(molecule):
    atom = ""
    count = 0
    while p < len(molecule) and not molecule[p].isdigit():
      if atom != "" and molecule[p].isupper():
        p-=1
        break
      atom += molecule[p]
      p +=1
    
    countString = ""
    while p < len(molecule) and molecule[p].isdigit():
      countString += molecule[p]
      p +=1

    if countString == "":
      count = coefficient * 1
    else:
      count = coefficient * int(countString)
      p-=1

    atoms[atom] = atoms.get(atom, 0) + count
    p+=1

  return atoms

def is_balanced(str):
  
  leftSide, rightSide = str.split("=")
  
  LMolecules = leftSide.replace(" ","").split("+")
  RMolecules = rightSide.replace(" ","").split("+")

  LAtoms = {}
  for molecule in LMolecules:
    coefficient = getCoefficient(molecule)
    LAtoms = getAtoms(molecule, coefficient, LAtoms)

  RAtoms = {}
  for molecule in RMolecules:
    coefficient = getCoefficient(molecule)
    RAtoms = getAtoms(molecule, coefficient, RAtoms)

  return LAtoms == RAtoms

'''
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

print(is_balanced("2H2 + O2 = 2H2O"))
print(not is_balanced("1000H2O = Au + Ag"))
print(is_balanced("H2O = H2O"))
print(is_balanced("2H2O2 = 2H2O + O2"))  

print(not is_balanced("NaCl = Na + Cl2"))
print(is_balanced("C6H12O6 + 6O2 = 6CO2 + 6H2O"))
print(is_balanced("12H2O = 12H2 + 6O2"))

'''
formation solution

from typing import Dict

def parse_molecule(molecule: str, counts: Dict[str, int]) -> Dict[str, int]:
    """
    Parse a single molecule string and update a dictionary of element counts.

    Args:
        molecule: A string representing a single molecule.
        counts: A dictionary representing the current element counts.

    Returns:
        A dictionary with updated element counts.
    """
    coefficient = 1
    i = 0
    while i < len(molecule):
        if molecule[i].isdigit():
            digit = ""
            while molecule[i].isdigit():
                digit += molecule[i]
                i += 1
            coefficient = int(digit)
        else:
            element = molecule[i]
            i += 1
            while i < len(molecule) and molecule[i].islower():
                element += molecule[i]
                i += 1
            count = ''
            while i < len(molecule) and molecule[i].isdigit():
                count += molecule[i]
                i += 1
            count = int(count) if count else 1
            count *= coefficient
            counts[element] = counts.get(element, 0) + count
    return counts

def parse_side(side: str) -> Dict[str, int]:
    """
    Parse a side of a chemical equation and return a dictionary of element counts.

    Args:
        side: A string representing a side of a chemical equation.

    Returns:
        A dictionary with element counts for the given side.
    """
    molecules = side.replace(" ", "").split('+')
    counts = {}
    for molecule in molecules:
        counts = parse_molecule(molecule, counts)
    return counts

def is_balanced(s: str) -> bool:
    """
    Check if a chemical equation is balanced.

    Args:
        s: A string representing a chemical equation.

    Returns:
        True if the equation is balanced, False otherwise.
    """
    lhs, rhs = s.split('=')
    left_counts = parse_side(lhs)
    right_counts = parse_side(rhs)
    return left_counts == right_counts
'''