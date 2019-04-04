import * from microbit
binary_string = '10001111010101001001100011110010'

asciistring = chr(int(binary_string[0:7], 2)) \
              + chr(int(binary_string[8:15], 2)) \
              + chr(int(binary_string[16:23], 2)) \
              + chr(int(binary_string[24:31], 2))
display.scroll(asciistring)