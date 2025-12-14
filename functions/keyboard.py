###
# Functions to read any data type from the keyboard
#
def input_string(message):
    message = str(input(message))
    return message

def input_integer(message):
    message = int(input(message))
    return message

def input_real(message):
    message = float(input(message))
    return message

def input_boolean(message):
    message = bool(input(message))
    return message