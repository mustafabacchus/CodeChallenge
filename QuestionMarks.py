q1 = 'acc?7??sss?3rr1??????5'      # True
q2 = 'arrb6???4xxbl5???eee5'       # True
q3 = '5??aaaaaaaaaaaaaaaaaaa?5?5'  # False
q4 = '9???1???9???1???9'           # True
q5 = 'aa6?9'                       # False


def question_marks(query):
    indices_of_pairs = []

    index = 0
    pair_indices = []
    for char in query:
        # Append index if digit
        if char.isdigit():
            pair_indices.append(index)
        # Append if pair of digits is made
        if len(pair_indices) == 2:
            indices_of_pairs.append(pair_indices)
            # Reset indices for next pair
            pair_indices = [index]
        index += 1

    sub_queries = []
    for pair_index in indices_of_pairs:
        # Check if pair is equal to 10
        num1 = query[pair_index[0]: pair_index[0] + 1]
        num2 = query[pair_index[1]: pair_index[1] + 1]
        if int(num1) + int(num2) == 10:
            # Extract and append center values of the pair
            sub_queries.append(query[pair_index[0] + 1: pair_index[1]])

    valid = False
    # Check if 3 marks are present per between pair values
    for sub_query in sub_queries:
        if len([char for char in sub_query if char == '?']) == 3:
            valid = True
        else:
            valid = False
            break
    return valid


print(question_marks(q1))
print(question_marks(q2))
print(question_marks(q3))
print(question_marks(q4))
print(question_marks(q5))
