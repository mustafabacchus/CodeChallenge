# 2
arr1 = [[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 2],
        [0, 0, 0, 2]]

# 1
arr2 = [[0, 0, 0],
        [1, 0, 0],
        [2, 0, 0]]

# 2
arr3 = [[0, 0, 0, 0],
        [2, 0, 1, 0],
        [0, 0, 0, 0],
        [2, 0, 0, 0]]

# 0
arr4 = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]


import math


def get_distance(data1, data2):
    points = zip(data1, data2)
    diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
    return math.sqrt(sum(diffs_squared_distance))


def closest_enemy(arr):
    enemies = []
    player = None

    # Find the position of the 1 and 2's
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 1:
                player = [row, col]
            if arr[row][col] == 2:
                enemies.append([row, col])

    if enemies:
        # Get the position of the closest 2
        shortest_distance = min([get_distance(player, enemy) for enemy in enemies])
        enemy = [enemy for enemy in enemies if get_distance(player, enemy) == shortest_distance].pop()

        moves = []
        while shortest_distance > 0:
            # Possible positions to move
            up = [player[0] - 1, player[1]] if player[0] != 0 else [len(arr) - 1, player[1]]
            down = [player[0] + 1, player[1]] if player[0] != len(arr[0]) - 1 else [0, player[1]]
            right = [player[0], player[1] + 1] if player[1] != len(arr[0]) - 1 else [player[0], 0]
            left = [player[0], player[1] - 1] if player[1] != 0 else [player[0], len(arr[0]) - 1]
            positions = [up, down, right, left]

            # Find the position that moves closest to the 2
            shortest_distance = min([get_distance(position, enemy) for position in positions])
            # Update the 1's position with the move
            player = [position for position in positions if get_distance(position, enemy) == shortest_distance].pop()
            moves.append(player)
        return len(moves)
    return 0


print(closest_enemy(arr1))
print(closest_enemy(arr2))
print(closest_enemy(arr3))
print(closest_enemy(arr4))

