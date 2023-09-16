# Exercise 3
## Demonstrate the use of the following Python data types
1. List
```python
people = ["Anna", "Baiba", "Dairis"] # initialize
people.pop() # remove last element
people[0] # access element
```
2. Dictionary
```python
people_ages = {
    "Anna": 35,
    "Baiba": 25,
    "Dairis": 100
} # initialize

people_ages.pop("Anna")  # remove
people_ages["Sandra"] = 55  # add
people_ages["Baiba"] # print value for key "Baiba" 
```
3. Set
```python
set1 = {"Windows", "Linux", "Mac"} # initialize in a hard coded way way
set2 = set(["Windows", "Linux", "Mac", "Linux"]) # initialize from list
set1.add("Android") # add
union_set = set1.union(set2) # merge
intersection_set = set1.intersection(set2) # the common values
difference_set = set1.difference(set2) # the unique values in set1
```
4. Tuple
```python
new_person = ("Edijs", 45) # initialize
name, age = new_person # access/unpack elements
new_people = new_person1 + new_person2 # merge tuples
```

### At the end of the main.py file there are more examples/experiments with these data types.