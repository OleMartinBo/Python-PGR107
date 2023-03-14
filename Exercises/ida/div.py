"""
        Diverse
"""
"""
        LIST
"""

#List input user:

def remove_min():
    my_list = []
 
    while True:
        user_input = input("Enter several integer to make a list ('Q' to exit): ")
        if user_input == "Q":
            break
        try:
            my_list.append(int(user_input))
        except ValueError:
            print("invalid input. Please enter an integer!")

    print("Your list: ", my_list)

remove_min()