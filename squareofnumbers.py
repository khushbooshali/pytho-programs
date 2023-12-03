def create_square_list(n):
    square_list = [i**2 for i in range(1, n+1)]
    return square_list
n = int(input())
result = create_square_list(n)
print(result)
