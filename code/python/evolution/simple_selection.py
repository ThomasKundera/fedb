#!/usr/bin/env python3

import random
from collections import defaultdict
import matplotlib.pyplot as plt

class Individual:
    def __init__(self, survival_rate, generation_born=0):
        self.survival_rate = max(0.0, min(1.0, survival_rate))  # Clamp between 0 and 1
        self.generation_born = generation_born

    def reproduce(self):
        """Produce 100 offspring with possible mutations"""
        offspring = []
        for _ in range(100):
            # Inherit parent's survival rate, then possibly mutate
            child_rate = self.survival_rate

            r = random.random()
            if r < 0.90:        # 90% neutral
                pass
            elif r < 0.949:     # 4.9% detrimental
                child_rate -= max(0.0, child_rate - 0.1)
            elif r < 0.999:     # 0.1% beneficial
                child_rate += min(1.0, child_rate + 0.001)
            offspring.append(Individual(child_rate, self.generation_born + 1))
        return offspring

    def survives(self):
        """Does this individual survive to reproduce next generation?"""
        return random.random() < self.survival_rate

    def __repr__(self):
        return f"Ind(sr={self.survival_rate:.2f})"


class Population:
    def __init__(self, initial_size=1000, max_size=100_000):
        self.individuals = [Individual(0.01) for _ in range(initial_size)]  # All start with 1% survival
        self.max_size = max_size
        self.generation = 0
        self.history = []  # Store avg survival rate per gen

    def run_generation(self):
        # 1. Reproduction: each surviving individual produces 100 offspring
        next_gen = []
        survivors = [ind for ind in self.individuals if ind.survives()]

        for parent in survivors:
            next_gen.extend(parent.reproduce())

        # 2. Population control: if too many, randomly cull to max_size
        if len(next_gen) > self.max_size:
            random.shuffle(next_gen)
            next_gen = next_gen[:self.max_size]

        # 3. Update population
        self.individuals = next_gen
        self.generation += 1

        # 4. Record statistics
        avg_sr = sum(ind.survival_rate for ind in self.individuals) / len(self.individuals)
        self.history.append({
            'generation': self.generation,
            'population': len(self.individuals),
            'avg_survival_rate': avg_sr,
            'max_survival_rate': max(ind.survival_rate for ind in self.individuals),
            'min_survival_rate': min(ind.survival_rate for ind in self.individuals)
        })

        print(f"Gen {self.generation:3d} | Pop: {len(self.individuals):6d} | "
              f"Avg survival: {avg_sr:.4f} | Max: {self.history[-1]['max_survival_rate']:.2f}")

    def run(self, generations=200):
        print("Starting simulation: rare beneficial mutations (0.5%) with strong selection\n")
        for _ in range(generations):
            self.run_generation()
            if self.history[-1]['avg_survival_rate'] > 0.99:
                print("Population has essentially fixed near-maximum fitness!")
                break

    def plot(self):
        gens = [h['generation'] for h in self.history]
        avg = [h['avg_survival_rate'] for h in self.history]
        max_sr = [h['max_survival_rate'] for h in self.history]

        plt.figure(figsize=(10, 6))
        plt.plot(gens, avg, label='Average survival rate', color='blue', lw=2)
        plt.plot(gens, max_sr, label='Best in population', color='green', alpha=0.7)
        plt.title('Evolution of Survival Rate\n(0.1% beneficial mutations with strong selection)')
        plt.xlabel('Generation')
        plt.ylabel('Survival Rate (fitness)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.ylim(0, 1)
        plt.show()


# ==================== RUN THE SIMULATION ====================
if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    pop = Population(initial_size=1000, max_size=10_000)
    pop.run(generations=20)
    pop.plot()
