# main.py
from fcfs import simulate_fcfs
from scan import simulate_scan
from sstf import simulate_sstf
import matplotlib.pyplot as plt


def get_inputs(need_direction=False):
    # 1. Get valid disk boundaries
    while True:
        try:
            disk_min = int(input("Enter Disk Minimum Cylinder (e.g., 0): "))
            disk_max = int(input("Enter Disk Maximum Cylinder (e.g., 250): "))
            if disk_min < 0 or disk_max <= disk_min: 
                print("Error: Maximum must be greater than minimum (and >= 0).")
                continue
            break
        except ValueError:
            print("Error: Please enter valid whole numbers.")

    # 2. Get valid initial head position
    while True:
        try:
            head = int(
                input(f"Enter Initial Head Position ({disk_min} - {disk_max}): ")
            )
            if head < disk_min or head > disk_max:
                print(
                    f"Error: Head must be between {disk_min} and {disk_max}."
                )
                continue
            break
        except ValueError:
            print("Error: Please enter a valid whole number.")

    # 3. Get valid request queue
    while True:
        raw_input = input(
            f"Enter Request Queue separated by spaces ({disk_min} - {disk_max}): "
        )
        parts = raw_input.replace(",", " ").split()

        if len(parts) == 0:
            print("Error: Queue cannot be empty.")
            continue

        try:
            queue = [int(num) for num in parts]
            out_of_range = [
                num for num in queue if num < disk_min or num > disk_max
            ]
            if out_of_range:
                print(
                    f"Error: {out_of_range} is outside {disk_min} - {disk_max}."
                )
                continue
            break
        except ValueError:
            print("Error: Queue must contain only whole numbers.")

    # 4. Get direction only if SCAN is chosen
    direction = None
    if need_direction:
        while True:
            direction = (
                input("Enter Initial SCAN Direction (up / down): ")
                .strip()
                .lower()
            )
            if direction in ["up", "down"]:
                break
            print("Error: Please type 'up' or 'down'.")

    return disk_min, disk_max, head, queue, direction


def print_table(algorithm_name, head, queue, sequence, steps, total_distance):
    queue_text = ", ".join(str(num) for num in queue)
    sequence_text = " -> ".join(str(num) for num in sequence)

    print("\nDISK SCHEDULING ALGORITHM")
    print(f"Current Head Position: {head}")
    print(f"Requests: {queue_text}")
    print(f"Service Sequence: {sequence_text}\n")

    print(algorithm_name.upper())
    print(f"{'STEP':<8} {'HEAD MOVEMENT':<20} {'DISTANCE':<10}")

    step_number = 1
    for start, end, distance in steps:
        movement = f"{start} - {end}"
        print(f"{step_number:<8} {movement:<20} {distance:<10}")
        step_number = step_number + 1

    print(f"{'':<8} {'TOTAL DISTANCE':<20} {total_distance:<10}")


def plot_head_movement(algorithm_name, sequence, disk_min, disk_max):
    # Create step numbers [0, 1, 2, ...] matching each stop in sequence
    step_numbers = list(range(len(sequence)))

    plt.figure(figsize=(9, 5))
    plt.plot(
        sequence,
        step_numbers,
        marker="o",
        linestyle="-",
        color="royalblue",
        linewidth=2,
    )

    # Label each dot with its exact cylinder number
    for step, cylinder in enumerate(sequence):
        plt.annotate(
            str(cylinder),
            (cylinder, step),
            textcoords="offset points",
            xytext=(0, -14),
            ha="center",
            fontsize=9,
            fontweight="bold",
        )

    # Format axes like a standard OS textbook diagram
    plt.xlim(disk_min, disk_max)
    plt.gca().invert_yaxis()  # Put Step 0 (Initial Head) at the top
    plt.yticks(step_numbers)
    plt.xlabel("Cylinder Number")
    plt.ylabel("Step Number")
    plt.title(f"{algorithm_name} - Disk Head Movement")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("\n========================================")
        print("DISK SCHEDULING SIMULATOR")
        print("========================================")
        print("1. FCFS")
        print("2. SSTF")
        print("3. SCAN (Elevator)")
        print("4. Exit")
        print("========================================")

        choice = input("Select Algorithm: ").strip()

        if choice == "1":
            d_min, d_max, head, queue, _ = get_inputs(need_direction=False)
            seq, steps, total = simulate_fcfs(head, queue)
            print_table(
                "FIRST COME, FIRST SERVE", head, queue, seq, steps, total
            )
            plot_head_movement("FIRST COME, FIRST SERVE", seq, d_min, d_max)

        elif choice == "2":
            d_min, d_max, head, queue, _ = get_inputs(need_direction=False)
            seq, steps, total = simulate_sstf(head, queue)
            print_table(
                "SHORTEST SEEK TIME FIRST", head, queue, seq, steps, total
            )
            plot_head_movement("SHORTEST SEEK TIME FIRST", seq, d_min, d_max)

        elif choice == "3":
            d_min, d_max, head, queue, direction = get_inputs(
                need_direction=True
            )
            seq, steps, total = simulate_scan(
                head, queue, d_min, d_max, direction
            )
            algo_title = f"SCAN ({direction.upper()})"
            print_table(algo_title, head, queue, seq, steps, total)
            plot_head_movement(algo_title, seq, d_min, d_max)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1 to 4.")


if __name__ == "__main__":
    main()