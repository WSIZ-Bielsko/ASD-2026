from dataclasses import dataclass
from random import randint, seed, random, sample


@dataclass
class Item:
    value: int
    weight: int



def random_items(n_elems: int)-> list[Item]:
    return [Item(value=randint(1,1001), weight=randint(1,1001)) for i in range(n_elems)]



def get_best_rucksack_composition(items: list[Item], max_weight: int) -> tuple[int, list[Item]]:
    # returns best value and rucksack composition
    return None


def get_best_rucksack_composition(items: list[Item], max_weight: int) -> tuple[int, list[Item]]:
    n = len(items)
    best_value = 0
    best_mask = 0

    for mask in range(1 << n):
        total_weight = 0
        total_value = 0
        for i in range(n):
            if mask & (1 << i):
                total_weight += items[i].weight
                if total_weight > max_weight:
                    break
                total_value += items[i].value
        else:
            if total_value > best_value:
                best_value = total_value
                best_mask = mask

    composition = [items[i] for i in range(n) if best_mask & (1 << i)]
    return best_value, composition


# --- genetic solution

def fitness(chromosome: list[int], items: list[Item], max_weight: int) -> int:
    total_weight = sum(c * it.weight for c, it in zip(chromosome, items))
    total_value = sum(c * it.value for c, it in zip(chromosome, items))
    if total_weight > max_weight:
        return 0
    return total_value


def random_chromosome(n: int) -> list[int]:
    return [randint(0, 1) for _ in range(n)]


def crossover(p1: list[int], p2: list[int]) -> list[int]:
    point = randint(1, len(p1) - 1)
    return p1[:point] + p2[point:]


def mutate(chromosome: list[int], mutation_rate: float = 0.02) -> list[int]:
    return [1 - g if random() < mutation_rate else g for g in chromosome]


def tournament_select(population: list[list[int]], fitnesses: list[int], k: int = 3) -> list[int]:
    selected = sample(list(zip(population, fitnesses)), k)
    return max(selected, key=lambda x: x[1])[0]


def genetic_get_best_rucksack_composition(
    items: list[Item],
    max_weight: int,
    population_size: int = 100,
    generations: int = 200,
    mutation_rate: float = 0.02,
    elitism: int = 2,
) -> tuple[int, list[Item]]:
    n = len(items)
    population = [random_chromosome(n) for _ in range(population_size)]

    best_chromosome = None
    best_fit = -1

    for _ in range(generations):
        fitnesses = [fitness(c, items, max_weight) for c in population]

        for c, f in zip(population, fitnesses):
            if f > best_fit:
                best_fit = f
                best_chromosome = c[:]

        # Elitism: keep top individuals
        ranked = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
        new_population = [c for c, _ in ranked[:elitism]]

        while len(new_population) < population_size:
            p1 = tournament_select(population, fitnesses)
            p2 = tournament_select(population, fitnesses)
            child = mutate(crossover(p1, p2), mutation_rate)
            new_population.append(child)

        population = new_population

    best_items = [it for gene, it in zip(best_chromosome, items) if gene == 1]
    return best_fit, best_items






if __name__ == '__main__':
    seed(111)
    items = random_items(25)
    max_weight = 2000
    # value, chosen = genetic_get_best_rucksack_composition(items, max_weight)
    value, chosen = get_best_rucksack_composition(items, max_weight)
    print(f"Best value: {value}")
    for it in chosen:
        print(it)