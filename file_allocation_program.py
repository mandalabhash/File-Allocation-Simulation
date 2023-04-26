# Set the number of blocks on the simulated disk
disk_size = 1000

# Set the number of time units to run the simulation
time_units = int(input("Enter the number of time units to run the simulation: "))

# Initialize the disk with all blocks free
disk = [0] * disk_size

def allocate_file(file_size):
    """Allocate space for a file on the disk using contiguous allocation."""
    # Find a free contiguous block of the required size
    start_block = -1
    free_blocks = 0
    for i in range(disk_size):
        if disk[i] == 0:
            free_blocks += 1
            if free_blocks == file_size:
                start_block = i - file_size + 1
                break
        else:
            free_blocks = 0

    # If a free contiguous block was found, allocate it
    if start_block != -1:
        for i in range(start_block, start_block + file_size):
            disk[i] = 1
        return True
    else:
        return False

def calculate_fragmentation():
    """Calculate and return the average amount of fragmentation on the disk."""
    free_blocks = 0
    fragments = 0
    for i in range(disk_size):
        if disk[i] == 0:
            free_blocks += 1
            if i == 0 or disk[i-1] == 1:
                fragments += 1

    if fragments == 0:
        return 0
    else:
        return free_blocks / fragments

def calculate_wasted_blocks():
    """Calculate and return the number of wasted disk blocks."""
    used_blocks = sum(disk)
    allocated_blocks = used_blocks + calculate_fragmentation()
    return disk_size - allocated_blocks

# Run the simulation for the specified number of time units
for t in range(time_units):
    # Allocate space for a random number of files with random sizes
    num_files = int(input("Enter the number of files to allocate: "))
    for i in range(num_files):
        file_size = int(input(f"Enter the size of file {i+1}: "))
        allocate_file(file_size)

    # Calculate and display the average amount of fragmentation and the number of wasted disk blocks
    avg_fragmentation = calculate_fragmentation()
    wasted_blocks = calculate_wasted_blocks()
    print(f"Time unit: {t+1}")
    print(f"Average fragmentation: {avg_fragmentation:.2f}")
    print(f"Wasted blocks: {wasted_blocks}")
