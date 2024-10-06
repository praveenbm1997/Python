# Function to get distance between two points
def get_distance(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    return (x * x) + (y * y)


# Function to check that points forms a square and parallel to the axis or not with the help get_distance function
def square_check(p1, p2, p3, p4):
    d2 = get_distance(p1, p2)
    d3 = get_distance(p1, p3)
    d4 = get_distance(p1, p4)

    if d2 == d3 and 2 * d2 == d4 and 2 * get_distance(p2, p4) == get_distance(p2, p3):
        return True

    if d3 == d4 and 2 * d3 == d2 and 2 * get_distance(p3, p2) == get_distance(p3, p4):
        return True

    if d2 == d4 and 2 * d2 == d3 and 2 * get_distance(p2, p3) == get_distance(p2, p4):
        return True

    return False


# Function to find all the squares which are parallel to  axis
def count(coordinates, v, n):
    total = 0
    vis = dict()

    # Loop to choose two points from the input
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            v1 = (v[i][0], v[i][1])
            v2 = (v[j][0], v[j][1])
            p1 = (v[i][0], v[j][1])
            p2 = (v[j][0], v[i][1])
            s = set()
            s.add(v1)
            s.add(v2)
            s.add(p1)
            s.add(p2)
            if len(s) != 4:
                continue

            # Condition to check if other points are present
            if p1 in coordinates and p2 in coordinates:
                if v1 not in vis or v2 not in vis or p1 not in vis or p2 not in vis:
                    if square_check(v[i], v[j], [v[i][0], v[j][1]], [v[j][0], v[i][1]]):
                        vis[v1] = 1
                        vis[v2] = 1
                        vis[p1] = 1
                        vis[p2] = 1

                        total += 1
    print(f'Number of square formed from the given co-ordinates is {total}')
    return total

# input
v = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
n = len(v)

# Function to Count the number of squares
def count_squares(v, n):
    coordinates = dict()

    # Adding the points
    for i in v:
        coordinates[(i[0], i[1])] = 1

    # calling the Count function to find the number of squares by sending the input co-ordinates and length of the input
    count(coordinates, v, n)

# Calling function to count the square
count_squares(v, n)


# time and space complexity:

# Time:
# There are two nested loops running for all input passed and then the square_check function runs with constant time O(n).
# So, time complexity of each loop is O(n^2).
# Therefore, the total time complexity is O(n^4).


# Space:
# The space complexity will depend on the input passed. So, the space complexity will be O(n).
