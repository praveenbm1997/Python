def disk_stacking(disks):
    # sorting  the disk based on height using lambda function
    disks.sort(key=lambda x: x[2])
    print(disks)
    heights = [disk[2] for disk in disks]
    sequence = [None for y in range(len(disks))]
    max_height = 0

    # looping through the disk input passed and also to compare the disks
    for i in range(1, len(disks)):
        current_disk = disks[i]
        for j in range(0, i):
            previous_disk = disks[j]

            # checking whether the current disk dimension is greater than previous disk by calling the disk_check function
            if disk_check(current_disk, previous_disk):

                # checking if my current disk height is less than combination of previous disk height
                if heights[i] <= heights[j] + current_disk[2]:
                    heights[i] = heights[j] + current_disk[2]
                    sequence[i] = j

# going through the height to get the maximum height
    for i in range(1, len(heights)):
        if heights[i] > heights[max_height]:
            max_height = i
    return get_disks(disks, sequence, max_height)


def disk_check(current_disk, previous_disk):
    # function helps in checking whether we can place disk one above the other by checking height, width and dept
    return current_disk[0] > previous_disk[0] and current_disk[1] > previous_disk[1] and current_disk[2] > previous_disk[2]


def get_disks(disks, sequence, max_height):
    # function will check and stack the disks
    stack = []
    while max_height is not None:
        stack.append(disks[max_height])
        max_height = sequence[max_height]
    print(stack)
    return list(stack)

# calling the disk stacking function
disk_stacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]])

# Time and space complexity


# Time:
# In disk_stacking function initially sorting will happen which will have O(log n).
# But, the two nested loops that compare every pair of disks take O(n^2) time.
# The inner loop, the disk_check function takes constant time, and update the heights and sequence lists also takes
# constant time & the loop that will assign index for sequence will take O(n)
# So, the overall time complexity is O(n^2)

# Space:
# The space complexity of the given is O(n).
# Since, it depends on the size of the input passed and sorted height and sequence will have the same length as input.
# So, the space complexity will remain O(n).

