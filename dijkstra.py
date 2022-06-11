import sys

vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]


def to_be_visited():
    global visited_and_distance
    v = -10
    for index in range(nov):
        if visited_and_distance[index][0] == 0 and (
                v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
            v = index
    return v


nov = len(vertices)
visited_and_distance = [[0, 0]]
for _ in range(nov - 1):
    visited_and_distance.append([0, sys.maxsize])

print(f"visited and distance {visited_and_distance}")
for i in range(nov):
    # Find next vertex to be visited
    to_visit = to_be_visited()
    print(to_visit)
    for neighbour_index in range(nov):
        # updating new distances
        if vertices[to_visit][neighbour_index] == 1 and visited_and_distance[neighbour_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbour_index]
            if visited_and_distance[neighbour_index][1] > new_distance:
                visited_and_distance[neighbour_index][1] = new_distance
        visited_and_distance[to_visit][0] = 1

i = 0

if __name__ == '__main__':
    for distance in visited_and_distance:
        print("Distance of ", chr(ord('a') + i), " from source vertex::: ", distance[1])
        i = i + 1
    print(f"New visited index {visited_and_distance}")