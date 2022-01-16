"""
Student Name : Achyut Krishna
Student ID   : 20ce120
Github Repository Link :https://github.com/Achyut-Krishna/Practical-2.git
University -> Charusat __ Chandubhai S. Patel Institute Of Technology

Index :
a. Write a Python program to add member(s) in a set and clear a set
b. Write a Python program to remove an item from a set if it is present in the set.
c. Write a Python program to create an intersection, Union, difference of sets.
d. Write a Python program to find maximum and the minimum value in a set.
e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

"""
"""Section 1. Write a Python program to add member(s) in a set and clear a set"""

c=set()
print(c)
print("element add")
c.add(1)
print(c)


"""Section 2. Write A python program to remove an item from the set."""

t={1,2,3}
t.remove(2)
print(t)

"""Section 3. Write A python program to to create an intersection, union and diffrence of set."""

s={1,2,3,4}
s1={4,3,5,6}
print("union",s,s1)
print("difference",s-s1)
print("intersection",s&s1)


"""Section 4. Write A python program to find max and min of the given value."""


s={1,2,3,4,5}
print(max(s))
print(min(s))

"""Section 5. Write A python program to find most common elements and their counts from tuple, list, dictionary."""

def IntersecOfSets(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    print('List = ',arr1)
    print('Tuple = ',arr2)
    print('Dictionary = ',arr3)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = set(result_set)
    print('common of members of list, tuple & dictionary =',final_list)

    if_name_=='__main__'
    list1 = [1, 2, 'ABC', 'xyz']
    tuple1 = (80, 50, 'ABC', 'xyz')
    dictionary1 = {300, 900, 'ABC', 'xyz'}
    IntersecOfSets(list1,tuple1,dictionary1)