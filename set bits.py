Question No 1 :- wap to count set Bits in an integer using functions.
                (the program finds the number of ones in the binary representstion
                of a number.)

def count_set_bits(number):
    binary_representation = bin(number)
    set_bits_count = binary_representation.count('1')
    return set_bits_count
num = int(input())
result = count_set_bits(num)
print(result)
