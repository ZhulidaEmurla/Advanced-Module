def are_parentheses_balanced(s):
    stack = []
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return "NO"

    return "YES" if not stack else "NO"


parentheses_sequence = input().strip()
result = are_parentheses_balanced(parentheses_sequence)
print(result)

