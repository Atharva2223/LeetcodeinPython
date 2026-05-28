class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        min_energy = min(enemyEnergies)
    
        if currentEnergy < min_energy:
            return 0
    
        total_energy = currentEnergy + sum(enemyEnergies) - min_energy
        return total_energy // min_energy