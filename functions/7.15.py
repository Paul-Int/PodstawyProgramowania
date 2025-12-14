def f(detector):
    people = 0
    max_people = 0

    for ch in detector:
        if ch == "+":
            people += 1
        elif ch == "-":
            people -= 1

        if people > max_people:
            max_people = people

    return max_people >= 3

print(f("+-+++-+---")) # True
print(f("+-+-+-+-")) # False
print(f("+-++-+--")) # False
print(f("+-++-++-+---")) # True