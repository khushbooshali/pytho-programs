Question No 3:- write a fuction that takes a list ad returns a new list with 
                unique elements of the first list and repeated elements will 
                be removed.

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list = [1,2,2,4,1,6,5]
result = remove_duplicates(input_list)
print(result)
