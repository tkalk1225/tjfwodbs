
def simulate_multi_species(species_params, generations):
    result = {}

    for name, N0, rate, uv_kill, phage_kill, resistance_rate in species_params:
        population = []
        current = N0
        resistance_ratio = 0.0

        for t in range(generations):
            current = int(current * (1 + rate))
            if t >= 5:
                resistance_ratio = min(0.8, resistance_ratio + resistance_rate)
            resistant = int(current * resistance_ratio)
            non_resistant = current - resistant
            non_resistant -= int(non_resistant * uv_kill)
            non_resistant -= int(non_resistant * phage_kill)
            current = max(0, non_resistant + resistant)
            population.append(current)

        result[name] = population
    return result
