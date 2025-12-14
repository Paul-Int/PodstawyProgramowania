def f(binary_number):
    if binary_number == "":
        return False
    for ch in binary_number:
        if ch != "0" and ch != "1":
            return False
    return True