def rpn_calculator():
    stack = []

    print("RPN calculator")
    print("Enter numbers, operators (+ - * /) or '=' to show result, 'q' to quit.")

    while True:
        token = input("> ").strip()

        if token.lower() == "q":
            break

        if token == "=":
            if len(stack) == 1:
                print("Result:", stack.pop())
            else:
                print("Error: stack should contain exactly one value.")
            stack = []
            continue

        if token in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                print("Error: not enough values on stack.")
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    print("Error: division by zero.")
                    stack.append(a)
                    stack.append(b)
                else:
                    stack.append(a / b)

        else:
            # number
            try:
                number = float(token)
                stack.append(number)
            except ValueError:
                print("Error: enter a number, an operator (+ - * /), '=' or 'q'.")


rpn_calculator()