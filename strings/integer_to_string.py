"""
Integer to string
Built-in functions used in the code

1) ord()
    The ord() function returns an integer representing the Unicode character.
    ord('0') - 48
    ord('1') - 49
    :
    :
    ord('9') - 57

2) chr()
    Python chr() function takes integer argument and return the string representing a character at that code point.
    chr(48) - '0'
    chr(49) - '1'
    :
    :
    chr(57) - '9'
"""

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return('-' if is_negative else '') + ''.join(reversed(s))


x = int(input("Enter the integer number to convert to string: "))
s = int_to_string(x)
print("The string after the conversion: ", s, "and its type: ", type(s))