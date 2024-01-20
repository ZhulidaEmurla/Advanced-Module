expressions = input()
paren_indexes = []

for index in range(0, len(expressions)):
    if expressions[index] == "(":
        paren_indexes.append(index)
    elif expressions[index] == ")":
        start_index = paren_indexes.pop()
        end_index = index + 1
        print(expressions[start_index:end_index])
