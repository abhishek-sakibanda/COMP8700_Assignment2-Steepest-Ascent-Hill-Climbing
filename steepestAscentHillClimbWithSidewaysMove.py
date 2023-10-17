import random


def initial_state():
    return [random.randint(0, 7) for _ in range(8)]


def cost(state):
    # Calculate the number of attacking pairs
    cost = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]):
                cost += 1
    return cost


def steepest_ascent_hill_climbing():
    max_attempts = 1000  # Maximum attempts to find a better move
    current_state = initial_state()
    current_cost = cost(current_state)
    steps = 0
    max_sideways = 100

    while current_cost > 0:
        best_moves = []
        best_cost = current_cost

        for col in range(8):
            for row in range(8):
                if current_state[col] != row:
                    new_state = list(current_state)
                    new_state[col] = row
                    new_cost = cost(new_state)

                    if new_cost < best_cost:
                        best_moves = [new_state]
                        best_cost = new_cost
                    elif new_cost == best_cost:
                        best_moves.append(new_state)

        if best_cost >= current_cost:
            max_sideways -= 1
            if max_sideways < 0:
                return False, steps
        else:
            max_sideways = 100

        if not best_moves:
            max_attempts -= 1
            if max_attempts <= 0:
                # If we can't find a better move, restart from a new random initial state
                return steepest_ascent_hill_climbing()
            current_state = initial_state()
            current_cost = cost(current_state)
        else:
            current_state = random.choice(best_moves)
            current_cost = best_cost
            steps += 1

    return True, steps


success_count = 0
failure_count = 0
total_steps_success = 0
total_steps_failure = 0

for _ in range(1000):
    success, steps = steepest_ascent_hill_climbing()
    if success:
        success_count += 1
        total_steps_success += steps
    else:
        failure_count += 1
        total_steps_failure += steps

success_rate = success_count / 1000
failure_rate = failure_count / 1000
average_steps_success = total_steps_success / success_count
average_steps_failure = total_steps_failure / failure_count

print("Success rate:", success_rate)
print("Failure rate:", failure_rate)
print("Average steps when succeeding:", average_steps_success)
print("Average steps when failing:", average_steps_failure)
