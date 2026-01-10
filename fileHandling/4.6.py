try:
    file_name = input("Enter file name: ")

    with open(file_name, 'r') as file:
        text = file.read()

    number_of_lines = text.count('\n') + 1
    number_of_characters = len(text)
    number_of_words = len(text.split())

    print("File name:", file_name)
    print("Number of lines:", number_of_lines)
    print("Number of characters:", number_of_characters)
    print("Number of words:", number_of_words)

except FileNotFoundError:
    print("Error: File does not exist.")