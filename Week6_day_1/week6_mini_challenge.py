################################list###################################################
# Lists Practice #1
# Print the following list on the screen:
# ["Python", "is", "easy", "to", "learn"]
",".join(["Python", "is", "easy", "to", "learn"])

# Lists Practice #1
# Create a list with 5 elements, inside the variable my_list. You can include strings, booleans, numbers, etc.
my_list_of_groceries  = ["milk" , "ceral" , " oatmeal" , "ham", "eggs"]

# Lists Practice #2
# Add the element "motorcycle" to the following list of means of transportation:
# transportation_means = ["plane", "car", "ship", "bicycle"]
# You must not modify the already supplied line of code, but must use the appropriate list method to add a new element.
transportation_means = [ " plane ", " car ", " ship ", " bicycle " ]
transportation_means.insert(4," motorcycle ")
print(transportation_means)
# Use the pop() method to remove the third item from the following list called fruits, and store it in a variable called deleted_item. Use list methods without altering the line of code already supplied.
# apple
# banana
# mango
# cherry
# watermelon
list_of_fruits = [" apples", " banana", " mango", " cherry", "watermelon"]
list_of_fruits.pop(2)
#######################################Dictionaries###############################
# Dictionaries Practice #1
# Create a dictionary called fruits with the following key-value pairs:
# apple --> red
# banana --> yellow
# mango --> green
# cherry --> red
# watermelon --> green
# Display the dictionary on the screen.
fruits = { " apples " : " red ", " banana ":" yellow ", " mango " :" green ", " cherry ":" red ", " watermelon ":" green " }
print(fruits)


# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist

my_dict = {
 "name": "Karen",
 "surname": "Jurgens",
 "age": "35",
 "occupation": "Journalist"
 }
print(my_dict)
# The names of the keys and values must be equal to the ones indicated above.

#   Dictionaries Practice #2
# Use print to returns the second item of the list called points2, inside the following dictionary.
# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
my_dict1 = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}

print(my_dict1["points"]) #Use dictionary indices to extract the second item of points2

# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombiait 
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}

my_dict.update({
    "country": "Colombia"})
print(my_dict)