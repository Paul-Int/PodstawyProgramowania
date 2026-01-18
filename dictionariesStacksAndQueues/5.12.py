def reverse_with_stack(text: str) -> str:
    stack = []
    for ch in text:
        stack.append(ch)  # push

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()  # pop

    return reversed_text


text = input("Enter text: ")
print("Reversed:", reverse_with_stack(text))