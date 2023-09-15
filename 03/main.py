# List
people = ["Anna", "Baiba", "Dairis"]

print(people)
print("Last person in the list is: ",people.pop())
print("First person in the list is: ",people[0])

# Dictionary
people_ages = {
    "Anna": 35,
    "Baiba": 25,
    "Dairis": 100
}

print(people_ages)
print("Baiba is ",people_ages["Baiba"], " years old")

# Set
set1 = {"Windows", "Linux", "Mac"}
# same as
set2 = set(["Windows", "Linux", "Mac", "Linux"])
print(set1)
print(set2)

# Tuple
new_person = ("Edijs", 45)
name, age = new_person

print(f"The new employee {name} is {age} years old.")
