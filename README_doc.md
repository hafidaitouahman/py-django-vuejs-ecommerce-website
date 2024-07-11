"# py-django-vuejs-ecommerce-website" 

psql -U postgres 
root2023
\c saulgadget-pgdb #use to database
\d list #tables

# Managing Application Dependencies
    Pipenv is a dependency manager for Python projects. If you’re familiar with Node.js’ npm or Ruby’s bundler, 
    it is similar in spirit to those tools. While pip alone is often sufficient for personal use, 
    Pipenv is recommended for collaborative projects as it’s a higher-level tool that simplifies
    dependency management for common use cases.
# Installing Pipenv
    windows: py -m pip install --user pipenv
    linux:   python3 -m pip install --user pipenv

# Installing packages for your project
    python -m pipenv install requests
    Pipenv will install the Requests library and create a Pipfile for you in your project’s directory. 
    The Pipfile is used to track which dependencies your project needs in case you need to re-install them, 
    such as when you share your project with others. You should get output similar to this (although the exact paths shown will vary):

# Using installed packages

    Now that Requests is installed you can create a simple main.py file to use it:

    import requests

    response = requests.get('https://httpbin.org/ip')

    print('Your IP is {0}'.format(response.json()['origin']))

    Then you can run this script using pipenv run:

    pipenv run python main.py

    You should get output similar to this:

    Your IP is 8.8.8.8

# Packaging your project
    win : py -m pip install build
    linux: python3 -m build --sdist

# Wheels 
    You should also create a wheel for your project. A wheel is a built package that can be installed without 
    needing to go through the “build” process. Installing wheels is substantially faster for the end user than installing 
    from a source distribution.

    If your project is pure Python then you’ll be creating a “Pure Python Wheel” (see section below).

    If your project contains compiled extensions, then you’ll be creating what’s called a *Platform Wheel* 

# You can use the following code to generate a requirements.txt file:
    pip install pipreqs
# then 
    pip3 freeze > requirements.txt  # Python3
    pip freeze > requirements.txt  # Python2
# or
    pipreqs /path/to/project (virtual env folder)
it generates a requirements.txt file :
attr==0.3.2
colorama==0.4.6
ConfigParser==7.0.0
cryptography==42.0.8
Django==5.0.6
docutils==0.21.2
filelock==3.15.4
HTMLParser==0.0.2
importlib_metadata==8.0.0
ipython==8.12.3
ipywidgets==8.1.3
jnius==1.1.0
keyring==25.2.1
Pillow==10.4.0
protobuf==5.27.2
pyOpenSSL==24.1.0
redis==5.0.7
Sphinx==7.3.7
thread==2.0.4
tornado==6.4.1
urllib3_secure_extra==0.1.0
xmlrpclib==1.0.1

# To install the requirements use:
    pip3 install -r requirements.txt

# install
    pip3 install pipreqs


# Run in current directory
    python3 -m  pipreqs.pipreqs .

    python2:
        pip install pipreqs
        python -m  pipreqs.pipreqs .

# To check your python version:
    python --version

# Before executing the above command make sure you have created a virtual environment.
    python3:
        pip3 install virtualenv
        python3 -m venv <myenvname> 
    python2:
        pip install virtualenv
        virtualenv <myenvname>


# To see what changes would be applied, without actually applying them:
	
	python manage.py makemigrations --dry-run --verbosity 3

	If you're happy with those changes, then run:
	python manage.py makemigrations

	Then run:
	python manage.py migrate

# What Does REPL in Python Mean? 

# Python offers an interactive REPL that you can use to communicate with your computer. The computer does these four tasks to make it work:

    Read your Python commands.
    Evaluate your code to work out what the input means.
    Print the results to see the computer’s response.
    Loop back to step 1 to keep communicating.

# PTP Python is considered to be the better or even the best Python REPL with Autocompletion, Autosuggestion, Docstring, and History Insertion. 

	To set up and install PTP Python, type:

	pip install ptpython

    Then, type:

        Ptpython
        On a standard Python shell, if you make a mistake and press Enter, you cannot go back and fix it. 
        Fortunately, ptpython lets you validate the input before pressing the Enter key.


# Indentation

    One of the main characteristics of Python is indentation. While other programming languages, 
    like Java and JavaScript, use braces to separate blocks of code, 
    Python code blocks are identified by different levels of line indentation.

# String methods:
    text = 'Hello, World!' # assign 'Hello, World!' to the variable text
    vulcan_greeting = ' Live long and prosper! ' # note the spaces at the start and end of the string
    list_of_strings = ['Nice', 'to', 'meet', 'you']
    
    ' '.join(list_of_strings) # join all the strings by the delimiter (in this case an empty space). Output: 'Nice to meet you'
    text.capitalize() # convert the first character to upper case. Output: 'Hello, world!'
    text.count('o') # return the number of occurrences of the specified substring. Output: 2
    text.endswith('o') # return True if the string ends with the specified substring. Output: False
    text.find('o') # return the lowest index of the specified substring. Output: 4 (the index starts with 0)
    text.islower() # return True if all cased characters are lowercase and the string contains at least one character. Output: False
    text.istitle() # return True if the string is titlecased and contains at least one character. Output: True
    text.isupper() # return True if the string is in uppercase and contains at least one character. Output: False
    vulcan_greeting.lstrip() # remove the left whitespace. Output: 'Live long and prosper!'
    text.lower() # convert the string into lower case. Output: 'hello, world!'
    text.replace('World', 'Universe') # return the string with all occurrences of the first substring replaced by the second substring. Output: 'Hello, Universe'
    vulcan_greeting.rsplit() # remove the right whitespace. Output ' Live long and prosper!'
    text.split() # split the string into separate words and return a list. Output: ['Hello,', 'World']
    vulcan_greeting.strip() # remove whitespace from both ends of the string. Output: 'Live long and prosper!'
    text.startswith('o') # return True if the string starts with the specified substring. Output: False
    text.swapcase() # swaps lower case to upper case and vice versa. Output: 'hELLO, wORLD'
    vulcan_greeting.title() # convert the first letter of each word to upper case. Output: 'Live Long And Prosper!'
    text.upper() # convert the string into upper case. Output: 'HELLO, WORLD!'

It is also possible to repeat strings by using the * operator: 
    greeting = 'Hello!'
    greeting * 3 # Output: Hello!Hello!Hello!

# Numeric: Integer and Float
    Using integer division with // results in an integer
    6 // 4 # Output: 1
    6.0 // 4 # Output: 1.0

# Conditional expressions
temperature_in_degrees_celsius = 20
sunny = temperature_in_degrees_celsius >= 20 # evaluates to True
cold = temperature_in_degrees_celsius <= 10 # evaluates to False

    if sunny: 
        print('Wear a t-shirt')
    elif cold:
        print('Wear a pullover and a jacket')
    else:
        print('More information needed to make a suggestion!')

    # Output: 'Wear a t-shirt'

# Python Built-in non-primitive data structures

Python provides several built-in non-primitive data structures to store and organize a collection of values.
# Dictionaries :
# Create an empty dictionary eng_ger 
eng_ger = {}

# Typecast an empty dictionary ger_eng
ger_eng = dict()

# Create a dictionary from two iterables
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_numbers = [1, 2, 3, 4, 5, 6, 7]

# zip both lists
weekdays_with_numbers = dict(zip(weekdays, weekday_numbers))
print(weekdays_with_numbers) # Output: {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

Adding, replacing, and deleting items:
# Add multiple key-value pairs to an empty dictionary
eng_ger = {'car': 'Automobil', 'house': 'Haus', 'cat': 'Katze'}
print(eng_ger) # Output: {'car': 'Automobil', 'house': 'Haus', 'cat': 'Katze'}

# Add a key-value-pair to an existing, non-empty dictionary
eng_ger['dog'] = 'Hund'
print(eng_ger) # output: {'car': 'Automobil', 'house': 'Haus', 'cat': 'Katze', 'dog': 'Hund'}
# Modify the value of an existing key
eng_ger['car'] = 'Auto'
print(eng_ger['car'] # Output: Auto

# Remove key-value pairs from a dictionary
del eng_ger['car']
print(eng_ger) # output: {'house': 'Haus', 'cat': 'Katze', 'dog': 'Hund'}  

# Remove all items from a dictionary
eng_ger.clear()
print(eng_ger) # Output: {}

Check whether a key or a value is contained in a dictionary:
# Check if a key is contained in a dictionary with the in keyword
print('mouse' in eng_ger) # Output: False

# Check if something appears as a value in a dictionary
values_in_dict = list(eng_ger.values()) # convert into list
print('Katze' in values_in_dict) # Output: True

Iterate over keys, values, and key-value pairs in dictionaries:
villains = {'Star Trek': 'The Borg', 'Star Wars': 'The Emperor', 'Harry Potter': 'Lord Voldemort', 'Lord of the Rings': 'Sauron'}

# iterate over the keys short version
for franchise in villains:
    print(franchise)

# Output:
Star Trek
Star Wars
Harry Potter
The Lord of the Rings
# iterate over the keys long version
For franchise in villains.keys():
    print(franchise) # Output: same as above

# iterate over the values
for villain in villains.values(): # the values() function must be called
    print(villain)

# Output:
The Borg
The Emperor
Lord Voldemort
Sauron

# iterate over the key-value pairs
for key, value in villains.items():
    print(f'Key: {key}, Value: {value}')

# Output:
Key: Star Trek, Value: The Borg
Key: Star Wars, Value: the Emperor
Key: Harry Potter, Value: Lord Voldemort

Get the number of key-value pairs in a dictionary:
# Get the number of key-value pairs in a dictionary
print(len(en_ger) # Output: 3

Merge multiple dictionaries into one dictionary:
villains = {'Star Trek': 'The Borg', 'Star Wars': 'The Emperor', 'Harry Potter': 'Lord Voldemort', 'Lord of the Rings': 'Sauron'}
more_villains = {'Star Trek TOS': 'Khan', 'Fantastic Beasts': 'Grindelwald', 'Star Wars': 'Darth Sidious'}

# In case of overlapping keys between the dictionaries, the newest value will be assigned to the key

# merge dictionaries with the update() function
villains.update(more_villains) # the villains dictionary is updated
print(villains)
# Output:
{'Star Trek': 'The Borg', 'Star Wars': 'Darth Sidious', 'Harry Potter': 'Lord Voldemort', 'Lord of the Rings': 'Sauron', 'Star Trek TOS': 'Khan', 'Fantastic Beasts': 'Grindelwald'}

# merge dictionaries with unpacking
combined_villains = {**villains, **more_villains} # a new dictionary is created and contains all values from the villains + more_villains dictionaries
print(combined_villains) # Output: same as above

# merge dictionaries with the dict() constructor
villains_combined = dict(villains, **more_villains) # the new dictionary takes the villains dictionary and combines it with the unpacked items of the more_villains dictionary
print(villains_combined) # Output: same as in the first example

# end dictionary

# Lists

Lists can contain zero or more items of different types. Like dictionaries, lists are mutable. Unlike dictionaries, the items in a list are indexed by their position, starting at 0. Lists can be sorted, reversed, sliced, and concatenated
# create an empty list
friends = []
pets = list()

# create a list with some items
favourite_colours = ['blue', 'black', 'orange']

Add and remove items:
# add an item at the end of a list
favourite_colours.append('green')
print(favourite_colours)
# Output: ['blue', 'black', 'orange', 'green']

# insert an item at a given position
favourite_colours.insert(1, 'yellow')
print(favourite_colours)
# Output: ['blue', 'yellow', 'black', 'orange', 'green']

# extend a list by appending another list
more_colours = ['red', 'grey', 'silver', 'purple']
favourite_colours.extend(more_colours)
print(favourite_colours)
# Output: ['blue', 'yellow', 'black', 'orange', 'green', 'red', 'grey', 'silver', 'purple']

# remove an item value from a list
favourite_colours.remove('yellow')
print(favourite_colours)
# Output: ['blue', 'black', 'orange', 'green', red', 'grey', 'silver', 'purple']

# remove the last item from a list
favourite_colours.pop()
print(favourite_colours)
# Output: ['blue', 'black', 'orange', 'green', red', 'grey', 'silver']

# remove an item at a given position from a list
favourite_colours.pop(3)
print(favourite_colours)
# Output: ['blue', 'black', 'orange', 'red', 'grey', 'silver']

# remove all items from a list
more_colours.clear()
print(more_colours)
# Output: []

Sort and reverse:
# sort a list alphabetically
favourite_colours.sort()
print(favourite_colours)
# Output: ['black', 'blue', 'grey', 'orange', 'red', 'silver']

# reverse a list
favourite_colours.reverse()
print(favourite_colours()
# Output: ['silver', 'red', 'orange', 'grey', 'blue', 'black']

Count:
# return the number of items in a list
print(len(favourite_colours)
# Output: 6

# return the number of occurrences of a specified value
print(favourite_colours.count('grey'))
# Output: 1
# end list


# Tuples
Like lists, the values in a tuple are indexed by integers, and tuples can contain elements of different types. 
The most important difference is that tuples are immutable. This means there are fewer functions available for tuples 
than for lists, because tuples can’t be modified. Why should tuples be used if they seem to be a light version of a list? 

    Tuples use less space than lists
    They can’t be changed by mistake
    They can be used as dictionary keys. This allows us to get a sorted version of a dictionary
    They are comparable

Create tuples:
# Enclose tuples in parentheses to make them quickly identifiable
vowels = ('a', 'e', 'i', 'o', 'u')

# When creating a tuple with a single element, a final comma has to be included to prevent it from being treated as a string
not_a_string = ('a',)

# Sets

Sets can consist of zero or more elements and can contain elements of different types. 
Sets are mutable and unordered collections that don’t allow duplicates. They are mostly used to test whether a value exists in the set, and to compute the union, intersection, difference, and symmetric difference of two sets.

Create sets:
vowels = {'a', 'e', 'i', 'o', 'u'}

# use the set() constructor for empty sets to avoid creating an empty dictionary
empty_set = set()

# test whether a value exists in a set
'y' in vowels
False

# add a single item
vowels.add('y')
print(vowels)
# Output: {'u', 'y', 'o', 'e', 'i', 'a'}

# add multiple items as a list
vowels.update('x', 'z', 'k')
print(vowels)
# Output: {'z', 'e', 'y' 'k', 'a', 'x', 'u', 'i', 'o'}

# remove a single item
vowels.discard('y')
print(vowels)
# Output: {'k','z', 'e', 'a', 'u', 'i', 'x', 'o'}
vowels.discard('x')
vowels.discard('z')
vowels.discard('k')

name = set('oscar')
# check for values in both sets
print(name.intersection(vowels)
# Output: {'o', 'a'}

# check for values that are in either set or both
print(name.union(vowels)
# Output: {'o', 'r', 'y', 'c', 'a', 'i', 'e', 'u', 's'}

# check for values that are in the first set but not the second
print(name.difference(vowels)
# Output: {'r', 's', 'c'}

# check for values that are in one of the sets, but not both of them
print(name.symmetric_difference(vowels)
# Output: {'r', 'y', 'c', 'e', 'u', 's', 'i'}

# end Sets


# Python Libraries

A Python library is a reusable collection of code or modules (a file with Python code in it) that can be used in programs or projects. 
The advantage lies in not having to write the code again and again. It is possible to simply import either separate functions 
or complete modules into our programs to make them available.
# import only the needed method
From math import sqrt
# import the complete module with all methods
import math


# The os module

#The functions in the os module allow interactions with the operating system.

import os

os.chdir('<path of directory>') # change current working directory
os.getcwd() # return the current working directory
os.listdir() # list the files and directories in the current working directory

# The math module allows access to the mathematical functions.

import math

x = 3.75

math.ceil(x) # return the smallest integer greater than or equal to x. Output = 4
math.floor(x) # return the largest integer less than or equal to x. Output = 3
math.sin(x) # return the sine of x radians. Output = -0.5715613187423437
math.sqrt(x) # return the square root of x. Output = 1.9364916731037085

# The random module is used for random selections.

import random

random.random() # returns a random float
random.randrange(12)) # returns a random integer in the range from 0 - 12
random.sample(range(100), 5)) # returns a list of 5 integers in the range from 0 - 100

Other modules provide tools for string pattern matching (import re), the calculation of statistical properties (import statistics), sending mail (import smtplib), manipulating dates and times (import datetime), and writing tests for functions or units (import doctest, import unittest).

Additionally, there are over 137,000 Python libraries available. The Python Package Index (PyPi) is a repository where users can find, install, and distribute Python software.





# How to create superuser in Django?

	python manage.py createsuperuser
	Then enter :
		Username: 
		Email address:
		Password:
		Password(again):

	