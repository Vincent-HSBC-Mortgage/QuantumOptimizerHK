# =====================================================
# QuantumOptimizerHK v3.1 - Production Ready
# Entropy-Enhanced Annealing for Personalized Optimization
# Calibrated Frequency: 432Hz | Matrix-96315013
# =====================================================

import numpy as np
import random
import math
from typing import Dict, List, Tuple

class QuantumField:
    """Enterprise-grade parameters for optimization field."""
    def __init__(self, mode: str = "Production"):
        self.version = "3.1.4"
        self.is_production = (mode == "Production")
        self.no_bar = True
        self.strict_budget = True
        self.elderly_friendly = False
        self.mood_boost = 1.2  # Enhanced resonance

# Resonant Frequencies (Hz) for Mood Calibration
MOOD_432HZ = {
    "HAPPY": 440, "CALM": 432, "FOCUS": 741, 
    "LUCKY": 528, "HUNGRY": 852, "ROMANTIC": 639
}

def compute_resonance_score(name: str, rating: float, budget_fit: float, 
                           vibe: List[str], mood: str = "CALM") -> float:
    """Calculates the 432Hz resonance score based on environmental factors."""
    # Base quality weight (40%)
    base_score = (rating / 5.0) * 0.4
    
    # Environmental vibe weight (30%)
    vibe_bonus = sum(0.15 for v in vibe if v.lower() in ["cozy", "quiet", "zen", "artistic"])
    
    # Frequency resonance factor
    hz_target = MOOD_432HZ.get(mood.upper(), 432)
    hz_factor = hz_target / 432.0
    
    # Final composite score (Normalized)
    return (base_score + (vibe_bonus * 0.3) + (budget_fit * 0.3)) * hz_factor

def entropy_anneal(scores: Dict[str, float], entropy: float = 0.15, seed: int = 96315013) -> Tuple[str, float, int]:
    """v3.1 Entropy-Enhanced Simulated Annealing for Global Optima."""
    np.random.seed(seed)
    random.seed(seed)
    
    candidates = list(scores.keys())
    if not candidates:
        return "No Node Found", 0.0, 0
        
    current_node = random.choice(candidates)
    current_val = scores[current_node] + np.random.normal(0, entropy)
    
    # Cooling schedule
    T, T_min, alpha = 1.5, 0.001, 0.88
    iterations = 0
    
    while T > T_min:
        next_node = random.choice(candidates)
        next_val = scores[next_node] + np.random.normal(0, entropy)
        delta = next_val - current_val
        
        # Metropolis Criterion
        if delta > 0 or random.random() < math.exp(delta / T):
            current_node, current_val = next_node, next_val
            
        T *= alpha
        iterations += 1
    
    return current_node, current_val, iterations

# =====================================================
# MAIN EXECUTION: Tsuen Wan Grid Calibration
# =====================================================
if __name__ == "__main__":
    # Real-world Data Nodes: Tsuen Wan District
    tsuen_wan_grid = {
        "The Mills - Cozy Cafe": compute_resonance_score("The Mills", 4.7, 0.8, ["cozy", "artistic"], "CALM"),
        "Lo Tak Court - Street Food": compute_resonance_score("Snacks", 4.3, 0.98, ["energetic"], "HAPPY"),
        "Nina Mall - Premium Dining": compute_resonance_score("Nina Mall", 4.5, 0.7, ["quiet", "zen"], "FOCUS"),
        "Sam Tung Uk - Heritage Noodles": compute_resonance_score("Old School", 4.2, 0.95, ["quiet"], "LUCKY")
    }
    
    winner, final_score, steps = entropy_anneal(tsuen_wan_grid)
    
    print("--- QuantumOptimizerHK v3.1 System Status ---")
    print(f"Targeting Logic: 432Hz Resonance")
    print(f"Quantum Winner: {winner}")
    print(f"Resonance Score: {final_score:.4f}")
    print(f"Optimization Steps: {steps}")
    print("---------------------------------------------")
