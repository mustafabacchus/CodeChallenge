# 1-0
arr1 = [['a', 'b', 'c', 'd'],
        ['e', 'i', 'k', 'r'],
        ['o', 'u', 'f', 'j']]

# 1-2
arr2 = [['a', 'q', 'r', 's', 't'],
        ['u', 'k', 'a', 'e', 'i'],
        ['f', 'f', 'o', 'o', 'o']]

# not found
arr3 = [['g', 'g'],
        ['f', 'f']]

# 0-0
arr4 = [['a', 'e', 'c', 'd', 'm'],
        ['e', 'i', 'k', 'r', 'k'],
        ['o', 'u', 'f', 'o', 'o'],
        ['g', 'c', 's', 'o', 'i']]


def vowel_square(arr):
    vowel_position = []

    # Row navigation
    row = 0
    col = 0
    while row < len(arr) - 1:
        # Column navigation
        if col < len(arr[0]) - 1:
            # Get the values in the square
            candidates = [arr[row][col], arr[row][col + 1],
                          arr[row + 1][col], arr[row + 1][col + 1]]
            # Check if values are vowels
            if len([char for char in candidates if char in ['a', 'e', 'i', 'o', 'u']]) == 4:
                # Append the position of the vowel square
                vowel_position.append([row, col])
            col += 1
        # Reset columns and increment row when columns are complete
        else:
            col = 0
            row += 1

    # Display results
    if not vowel_position:
        return 'not found'
    # Get the top left most vowel square
    top_left = min(vowel_position)
    return str(top_left[0]) + '-' + str(top_left[1])


print(vowel_square(arr1))
print(vowel_square(arr2))
print(vowel_square(arr3))
print(vowel_square(arr4))
