# Day 2: 30days of python programming
first_name = "Wisdom"
last_name = "Ebong"
full_name = "Wisdom Ebong"
country = "Nigeria"
city = "Kano"
age = "250"
year = 2025
is_married = False
is_true = False
is_light_on = True
first_name, last_name, age, country = "Wisdom", "Ebong", "250", "Nigeria"

#checking the data type of all variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

first_name = "Wisdom"
length_of_first_name = len(first_name)
print(len(first_name))

first_name = "Wisdom"
last_name = "Ebong"
length_of_first_name = len(first_name)
length_of_last_name = len(last_name)
print(len(first_name))
print(len(last_name))

if length_of_first_name > length_of_last_name:
    print("first name is longer than last name")
elif length_of_first_name < length_of_last_name:
    print("last name is longer than first name")
else:
    print("first name and last name are equal length")