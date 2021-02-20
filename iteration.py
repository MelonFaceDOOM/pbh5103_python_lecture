some_numbers = [1,2,3] # list example 
my_name = "jacob miller" # string example

# dict example. {[key]: [value]}
movie_directors = { 
    "interstellar": "christopher nolan", 
    "rear window": "alferd hitchcock",
    "mad max: fury road": "george miller",
    "back to the future": "robert zemeckis"
}

lol = [["a",1],["b",2],["c",3],["d",4]] # list of lists

def loop_through_list():
    for thingy in some_numbers:
        print(thingy)
    print('\n')

def loop_through_string():
    for character in my_name:
        print(character)
    print('\n') # ex1: try indenting this to see how it changes the output.

def use_dict():    
    print(movie_directors["mad max: fury road"])
    # ex2: how do you iterate over each item in a dict? Google it!

def lol_1():
    for pair in lol:
    # do not use "list" as a variable name, since it is a python keyword.
    # keywords can be found here:
    # https://www.programiz.com/python-programming/keyword-list
        print(pair)
    
def lol_2():
    for pair in lol:
        for item in pair:
            print(item)
            
def lol_3():
    for a,b in lol:
        print(f"{a} is a letter and {b} is a number")
        
# while loop
def while_loop():
    a = 100
    while a > 75:
        print(a)
        a -= 12 # equivalent to: a = a-12
    print(f"a is now {a}") # this is an f-string. variables can be placed inside {}

# loop_through_list()
# loop_through_string()
# use_dict()
# lol_3()
# lol_1()
# lol_2()
# while_loop()