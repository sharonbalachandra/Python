# I want a dictionary where I can ask what breed our dogs are

def question():
    user_input = input('Name the pet you would like to find the breed for? \n')
    return user_input


def breed_finder(dog):
    dict_breed={"Cherri":"Pomeranian","Myllo":"Cockapoo","Caesar":"German Husky","Twinkle":"Golden Lab"}
    print(dog, "is a", dict_breed[dog])


if __name__ == '__main__': 
    dog_name = question()
    breed_finder(dog_name)


# Step 1: Define a new function for asking a question.
# The question gets asked and the name will be typed in by the user.
# The user response will be stored as a variable called "user_input".
# We use return so that the variable "user_input" is extracted out of the function.
# 
# Step 2: Define a new function for the logic, with an compulsory argument "dog". Without the variable "dog", the function will not run.
# Define dictionary with key-value pairs.
# Define print statement for the pet set as the variable "dog".
# 
# Step 3: Use if __name__ == '__main__' for good practice, as it runs only the specific code that you want within the module.
# Define the variable "dog_name" as equal to the returned value of the function question().
# Pass the "dog_name" into the "breed_finder" function to find out what breed the specific dog is.
