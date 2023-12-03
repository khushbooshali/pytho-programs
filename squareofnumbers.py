 Question No 4 :-write a function to create and print a list where 
                  the values are square of numbers betwween 1 and n 
                 (both included).
                  
def create_square_list(n):
    square_list = [i**2 for i in range(1, n+1)]
    return square_list
n = int(input())
result = create_square_list(n)
print(result)

