


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions = sorted(potions)
        print(spells, potions)
        successfulPairs = []

        for spell in spells:

            left = 0 
            right = len(potions) - 1
            


            while left < right:
                #print(spell, left, right, mid)
                mid = (left+right) //2
                product = potions[mid] * spell
                if product >= success:
                    right = mid
                else:
                    left = mid + 1
            
            if potions[left] * spell >= success:
                successfulPairs.append(len(potions) - left)
            else:
                successfulPairs.append(0)

                





        return successfulPairs