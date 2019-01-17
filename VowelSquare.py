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
    def is_vowel(char):
        return char in ['a', 'e', 'i', 'o', 'u']

    row = 0
    col = 0
    col_len = len(arr[0]) - 1
    row_len = len(arr) - 1
    vowel_pos = []

    # Row navigation
    while row < row_len:
        # Column navigation
        if col < col_len:
            # Get the values in a square
            char1 = arr[row][col]
            char2 = arr[row][col + 1]
            char3 = arr[row + 1][col]
            char4 = arr[row + 1][col + 1]
            # Check if values are vowels
            if is_vowel(char1) and is_vowel(char2) and \
                    is_vowel(char3) and is_vowel(char4):
                # Append the position of the vowel square
                vowel_pos.append([row, col])
            col += 1
        # Reset columns and increment row when columns are complete
        else:
            col = 0
            row += 1

    # Display results
    if not vowel_pos:
        return 'not found'
    # Get the top left most vowel square
    top_left = min(vowel_pos)
    return str(top_left[0]) + '-' + str(top_left[1])


print(vowel_square(arr1))
print(vowel_square(arr2))
print(vowel_square(arr3))
print(vowel_square(arr4))
