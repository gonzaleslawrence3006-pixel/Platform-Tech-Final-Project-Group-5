def simulate_sstf(head, queue):
    current = head
    total_movement = 0
    sequence = [head]
    steps = []

    while queue:
        # Find the closest request to the current head position
        closest_request = min(queue, key=lambda req: abs(req - current)) 
        distance = abs(closest_request - current)
        steps.append((current, closest_request, distance))
        total_movement += distance
        current = closest_request
        sequence.append(current)
        queue.remove(closest_request) 

    return sequence, steps, total_movement

def print_schedule_table(algo_name, head, queue, steps, total_movement):
    print("\nDISK SCHEDULING ALGORITHM")
    print(f"Current Head Position: {head}")
    print(f"Requests: {', '.join(map(str, queue))}\n")

    print(algo_name.upper())
    print(f"{'STEP':<8} {'HEAD MOVEMENT':<20} {'DISTANCE':<10}")

    for step_num, (src, dst, dist) in enumerate(steps, start=1):
        movement_str = f"{src} - {dst}"
        print(f"{step_num:<8} {movement_str:<20} {dist:<10}")

    print(f"{'':<8} {'TOTAL DISTANCE':<20} {total_movement:<10}")
