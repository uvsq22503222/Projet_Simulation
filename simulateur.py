from dataclasses import dataclass
import heapq
import numpy as np


ARRIVAL = "arrival"
START_TX = "start_tx"
END_TX = "end_tx"


@dataclass
class SimulationResult:
    times: list
    throughput: list
    mean_clients: list
    loss_rate: list
    collision_rate: list
    final_throughput: float
    collisions: int
    losses: int
    arrivals: int
    successes: int


def expo_mean(mean, rng):
    return rng.exponential(mean)


def schedule(event_queue, time, event_type, station):
    heapq.heappush(event_queue, (time, event_type, station))


def simulate(N, K, lambd, tau, T, seed=None, exponential_backoff=True):

    rng = np.random.default_rng(seed)

    queues = [0] * N
    backoff_state = [1] * N
    transmitting = [False] * N
    collided = [False] * N
    scheduled_start = [False] * N

    event_queue = []

    successes = 0
    losses = 0
    arrivals = 0
    collisions = 0

    times = []
    throughput_values = []
    mean_clients_values = []
    loss_rate_values = []
    collision_rate_values = []

    for s in range(N):
        first_arrival = expo_mean(1 / lambd, rng)
        schedule(event_queue, first_arrival, ARRIVAL, s)

    while event_queue:

        current_time, event_type, station = heapq.heappop(event_queue)

        if current_time > T:
            break

        if event_type == ARRIVAL:

            arrivals += 1

            next_arrival = current_time + expo_mean(1 / lambd, rng)

            if next_arrival <= T:
                schedule(event_queue, next_arrival, ARRIVAL, station)

            if queues[station] >= K:
                losses += 1

            else:
                queues[station] += 1

                if not transmitting[station] and not scheduled_start[station]:
                    scheduled_start[station] = True
                    schedule(event_queue, current_time, START_TX, station)

        elif event_type == START_TX:

            scheduled_start[station] = False

            if queues[station] <= 0:
                continue

            transmitting[station] = True
            collided[station] = False

            active = [
                s for s in range(N)
                if transmitting[s] and s != station
            ]

            if active:
                collided[station] = True
                collisions += 1

                for other in active:
                    collided[other] = True

            schedule(event_queue, current_time + 1, END_TX, station)

        elif event_type == END_TX:

            transmitting[station] = False

            if queues[station] <= 0:
                continue

            if collided[station]:

                i = backoff_state[station]

                if exponential_backoff:
                    delay = expo_mean((2 ** i) * tau, rng)
                else:
                    delay = expo_mean(tau, rng)

                backoff_state[station] += 1

                scheduled_start[station] = True
                schedule(event_queue, current_time + delay, START_TX, station)

            else:

                successes += 1

                queues[station] -= 1

                backoff_state[station] = 1

                if queues[station] > 0:
                    scheduled_start[station] = True
                    schedule(event_queue, current_time, START_TX, station)

        times.append(current_time)

        if current_time > 0:
            throughput_values.append(successes / current_time)
            collision_rate_values.append(collisions / current_time)
        else:
            throughput_values.append(0)
            collision_rate_values.append(0)

        total_clients = sum(queues)
        mean_clients_values.append(total_clients / N)

        if arrivals > 0:
            loss_rate_values.append(losses / arrivals)
        else:
            loss_rate_values.append(0)

    return SimulationResult(
        times=times,
        throughput=throughput_values,
        mean_clients=mean_clients_values,
        loss_rate=loss_rate_values,
        collision_rate=collision_rate_values,
        final_throughput=successes / T,
        collisions=collisions,
        losses=losses,
        arrivals=arrivals,
        successes=successes
    )