import * from microbit
binary_string = '10001111010101001001100011110010'

int_signed = int(binary_string[1:], 2)
if binary_string[0] == '1':
    int_signed = int_signed * (-1)
display.scroll(int_signed)