def simulate_scan(head, queue, disk_min, disk_max, direction):
    current = head
    total_movement = 0
    sequence = [head]
    steps = []

    downward = []
    for req in queue:
        if req < head:
            downward.append(req)
    downward.sort(reverse=True)

    upward = []
    for req in queue:
        if req >= head:
            upward.append(req)
    upward.sort()

    if direction == "down":
        # 1. Service all downward requests first
        for req in downward:
            distance = abs(req - current)
            steps.append((current, req, distance))
            total_movement += distance
            current = req
            sequence.append(current)

        if upward and current != disk_min:
            distance_to_min = abs(disk_min - current)
            steps.append((current, disk_min, distance_to_min))
            total_movement += distance_to_min
            current = disk_min
            sequence.append(current)

        for req in upward:
            distance = abs(req - current)
            steps.append((current, req, distance))
            total_movement += distance
            current = req
            sequence.append(current)

    elif direction == "up":
        # 1. Service all upward requests first
        for req in upward:
            distance = abs(req - current)
            steps.append((current, req, distance))
            total_movement += distance
            current = req
            sequence.append(current)

        if downward and current != disk_max:
            distance_to_max = abs(disk_max - current)
            steps.append((current, disk_max, distance_to_max))
            total_movement += distance_to_max
            current = disk_max
            sequence.append(current)

        for req in downward:
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
