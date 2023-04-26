# File-Allocation-Simulation
File Allocation Simulation Project for Academic fulfillment of Operating Systems at LPU, Punjab



Question/ Problem Statement

Scenario: A company has a large number of employees who work on various projects and create different types of files such as documents, spreadsheets, and images. The company wants to implement a new file system that can manage the disk space efficiently and handle the high volume of file operations.

Problem: Create a simulation program that simulates a file system for the company. The program should include a file system manager that uses a specific file allocation algorithm (e.g. Contiguous Allocation or Linked Allocation) to allocate space for files on a simulated disk. The students should also include a mechanism for deleting, renaming and moving files. The simulation should run for a set amount of time and record the average amount of fragmentation and the number of wasted disk blocks at the end of each time unit.
Consider the following factors in their simulation:

• The employees will be creating and editing different types of files (e.g. documents, spreadsheets, images) with varying file sizes.

• The employees will be frequently adding and deleting files.

• The company wants to minimize the amount of wasted disk space.

Provide a report on their findings and observations, including the performance of the file system under different scenarios and the trade-offs involved in the different file allocation algorithms (Contiguous or Linked Allocation).
Expected outcomes:

1. File allocation: The program should demonstrate the ability to allocate space for files on a simulated disk using the chosen file allocation algorithm (e.g. Contiguous Allocation or Linked Allocation).
The program should run the simulation for a set amount of time and display the results, including the average amount of fragmentation and the number of wasted disk blocks, at the end of each time unit.




Methodology Adopted to Solve the Problem


The simulation was implemented using Python Language.
The steps followed were:
1.	Set the size of the simulated disk to 1000.
2.	Ask the user to enter the number of time units to run the simulation.
3.	Initialize the disk by creating a list of 1000 zeros.
4.	Define a function called allocate_file that takes a file size as an argument and tries to allocate a contiguous block of the required size on the disk. The function does this by iterating over the disk, looking for a sequence of free blocks of the required size. If it finds one, it marks the blocks as used by setting their values to 1, and returns True. If it can't find a contiguous block of the required size, it returns False.
5.	Define a function called calculate_fragmentation that calculates the average amount of fragmentation on the disk. It does this by iterating over the disk, counting the number of free blocks and the number of fragments (i.e., groups of contiguous free blocks separated by used blocks). It then divides the number of free blocks by the number of fragments to get the average amount of fragmentation.
6.	Define a function called calculate_wasted_blocks that calculates the number of wasted disk blocks. It does this by adding up the number of used blocks and the average amount of fragmentation (as calculated by the calculate_fragmentation function), and subtracting the result from the total size of the disk.
7.	Run the simulation for the specified number of time units. For each time unit, the program asks the user to enter the number of files to allocate, and for each file, it asks for the file size and tries to allocate a contiguous block of that size on the disk using the allocate_file function. It then calculates and displays the average amount of fragmentation and the number of wasted blocks for that time unit.
