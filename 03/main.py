# List
print("--------------Some examples with lists------------------")
people = ["Anna", "Baiba", "Dairis"]

print(people)
print("Last person in the list is: ", people.pop()) # remove and print the last
print("First person in the list is: ", people[0])

# Dictionary
print("------------Some examples with dictionaries--------------")
people_ages = {
    "Anna": 35,
    "Baiba": 25,
    "Dairis": 100
}

people_ages.pop("Anna")  # remove
people_ages["Sandra"] = 55  # add
print(people_ages)
print("Baiba is ", people_ages["Baiba"], " years old")

# Set
print("--------------Some examples with sets------------------")
set1 = {"Windows", "Linux", "Mac"}
# same as
set2 = set(["Windows", "Linux", "Mac", "Linux"])
print(set1, "=",set2)
set1.add("Android")
print("Updated set:",set1)

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

difference_set = set1.difference(set2)
print("Elements in set1 but not in set2:", difference_set)

# Tuple
print("-------------Some examples with tuples-----------------")

new_person1 = ("Edijs", 45)
name, age = new_person1
new_person2 = ("Sandra", 26)
new_people = new_person1 + new_person2

print(f"The new employee {name} is {age} years old.")
print("All new people: ", new_people)

# Interactions
print("-------------Some interactions between the types and cooler examples-----------------")

# Check the age of everyone in the list
print("There are ",len(people), " people in the list.")
for person in people:
    if person in people_ages:
        age = people_ages[person]
        print(f"{person} is {age} years old.")
    else:
        print(f"{person} is unknown.")


# Creating a new list of people's names from the dictionary keys
print("------------")
people_names = list(people_ages.keys())
print("List of people's names from the dictionary:", people_names)

# Getting the average age of people in the dictionary
print("------------")
age_sum = 0
people_count = 0

for age in people_ages.values():
    age_sum += age
    people_count += 1

if people_count > 0:
    average_age = age_sum / people_count
    print(f"The average age of the {people_count} people in the dictionary is {average_age:.0f} years.")
