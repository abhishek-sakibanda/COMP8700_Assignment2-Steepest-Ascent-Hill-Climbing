import random


def evaluate(state):
    # Initialize the conflict count.
    conflicts = 0

    for col in range(8):
        for next_col in range(col + 1, 8):
            # Check horizontal conflicts.
            if state[col] == state[next_col]:
                conflicts += 1
            # Check diagonal conflicts.
            if abs(state[col] - state[next_col]) == next_col - col:
                conflicts += 1

    return conflicts


def steepest_ascent_hill_climbing(max_steps):
    steps = 0
    current_state = generate_random_state()
    current_fitness = evaluate(current_state)

    while steps < max_steps and current_fitness > 0:
        best_successor = current_state
        best_fitness = current_fitness

        for col in range(8):
            for row in range(8):
                if current_state[col] == row:
                    continue  # Skip the current position.
                successor = list(current_state)  # Copy the current state.
                successor[col] = row  # Move the queen to a new row.
                successor_fitness = evaluate(successor)

                if successor_fitness < best_fitness:
                    best_successor = successor
                    best_fitness = successor_fitness

        if best_fitness >= current_fitness:
            break

        current_state = best_successor
        current_fitness = best_fitness
        steps += 1

    return current_state, current_fitness, steps


def generate_random_state():
    # Generate a random initial state.
    return [random.randint(0, 7) for _ in range(8)]


def generate_successors(state):
    # Generate successor states by moving queens.
    successors = []

    for col in range(8):
        for row in range(8):
            if state[col] == row:
                continue  # Skip the current position.
            successor = list(state)  # Copy the current state.
            successor[col] = row  # Move the queen to a new row.
            successors.append(successor)

    return successors


success_steps = 0
failure_steps = 0
success_count = 0

for _ in range(1000):
    solution, fitness, steps = steepest_ascent_hill_climbing(max_steps=1000)
    if fitness == 0:
        success_steps += steps
        success_count += 1
    else:
        failure_steps += steps

print("Average steps for success:", success_steps / success_count)
print("Average steps for failure:", failure_steps / (1000 - success_count))
print("Success count:", success_count)
print("Failure count:", 1000 - success_count)
