Question no 2 :- wap to display all keys and values of a dictionary 

def display_dict(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")
my_dict = {'ramu':25,'ajay':5,'satya':50}
display_dict(my_dict)
