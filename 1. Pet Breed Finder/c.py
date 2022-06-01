# I want a dictionary where I can ask what breed our dogs are

def breed_finder():
    dog = input('Name the pet you would like to find the breed for? \n')
    dict_breed={"Cherri":"Pomeranian","Myllo":"Cockapoo","Caesar":"German Husky","Twinkle":"Golden Lab"}
    print(dog, "is a", dict_breed[dog])


breed_finder()


# Step 1: Define a new function for finding the breed. 
# This function should ask the user what pet they would like to find the breed for. The user response will be stored as a variable called "dog".
# Define dictionary with key-value pairs.
# Define print statement for the pet set as the variable "dog".
# 
# Step 2: Call the function.
