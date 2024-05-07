def convert_to_binary(decimal):
    return bin(decimal)

def convert_to_hexadecimal(decimal):
    return hex(decimal)

def convert_to_octal(decimal):
    return oct(decimal)

def generate_custom_NIMs(base_NIM):
    custom_NIMs = []
    for i in range(5):
        custom_NIM = base_NIM[:-3] + str(i) + str(i+1) + str(i+2)
        custom_NIMs.append(custom_NIM)
    return custom_NIMs

base_NIM = "23090161"
binary = convert_to_binary(int(base_NIM))
hexadecimal = convert_to_hexadecimal(int(base_NIM))
octal = convert_to_octal(int(base_NIM))
custom_NIMs = generate_custom_NIMs(base_NIM)

print("Base NIM:", base_NIM)
print("Binary:", binary)
print("Hexadecimal:", hexadecimal)
print("Octal:", octal)
print("Custom NIMs:", custom_NIMs)
