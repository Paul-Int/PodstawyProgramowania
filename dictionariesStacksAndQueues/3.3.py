expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"   # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct


def brackets_ok(expression: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())
    closing = set(pairs.keys())

    for ch in expression:
        if ch in opening:
            stack.append(ch)  # push
        elif ch in closing:
            if not stack:
                return False
            top = stack.pop()  # pop
            if top != pairs[ch]:
                return False

    return len(stack) == 0  # True if all opened were closed


# Check expressions
for i, expr in enumerate([expression1, expression2, expression3], start=1):
    if brackets_ok(expr):
        print(f"expression{i}: brackets OK")
    else:
        print(f"expression{i}: brackets NOT correct")