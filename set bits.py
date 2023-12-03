def count_set_bits(number):
    binary_representation = bin(number)
    set_bits_count = binary_representation.count('1')
    return set_bits_count
num = int(input())
result = count_set_bits(num)
print(result)
