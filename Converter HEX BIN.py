def binary_to_hex(b3, b2, b1, b0):
    # juntar os bits
    binary_string = f"{b3}{b2}{b1}{b0}"
    
    # converter para inteiro
    bin_num = int(binary_string, 2)
    
    # converter para hexadecimal
    hex_value = hex(bin_num)

    # saída em 4 bits
    hex_out = format(bin_num, '04b')

    return bin_num, hex_value, hex_out


# exemplo de uso
b3, b2, b1, b0 = 1, 0, 1, 1

num, hex_value, hex_out = binary_to_hex(b3, b2, b1, b0)

print("Número decimal:", num)
print("Hexadecimal:", hex_value)
print("Saída 4 bits:", hex_out)