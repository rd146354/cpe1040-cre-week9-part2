import * from microbit
binary_string = '10001111010101001001100011110010'

mantissa = 0.0
bias = 127
if binstr[0] == '1':
    sign = -1
else:
    sign = 1

exponent = int(binstr[1:9], 2)
exponent -= bias
for bit in range(31, 9, -1):
    if binstr[bit] == '1':
        break
mantissa_string = binstr[9:bit + 1]
for bit in range(0, len(mantissa_string)):
    if mantissa_string[bit] == '1':
        mantissa = mantissa + (2 ** (-1 * (bit + 1)))
float_out = (sign * 2 ** exponent * (1 + mantissa))
display.scroll(float_out)