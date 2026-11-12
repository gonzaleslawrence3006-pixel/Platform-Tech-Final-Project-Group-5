def simulate_fcfs(head, queue): 
    current = head
    total_movement = 0
    sequence = [head]
    steps = []

    for req in queue:
        distance = abs(req - current) 
        steps.append((current, req, distance)) 
        total_movement += distance
        current = req 
        sequence.append(current)

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
