# Python exam revision


The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

```
def open_or_senior(data):
    output_list = []
    for age_handi in data:
        if age_handi[0] >= 55 and age_handi[1] > 7:
            output_list.append("Senior")
        else:
            output_list.append("Open")
            
    return output_list
```


In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```
def filter_list(l):
    int_list = []
    for item in l:
        if type(item) == int:
            int_list.append(item)
    return int_list
```

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

```
def duplicate_encode(word):
    return_string =""
    word = word.lower()
    for letter in word:
        if word.count(letter) == 1:
            return_string += "("
            
        else:
            return_string += ")"
            
    return return_string
```

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
```
from math import sqrt 
def find_next_square(sq):
    square_root = sqrt(sq)
    if square_root.is_integer():
        return (square_root+1) * (square_root+1) 
    else:
        return -1
```

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
```
def split(word):
    return [char for char in word]

def accum(s):
    n = -1
    seperate_list = []
    list_of_chars = split(s)
    for x in range(len(list_of_chars)):
        if x == 0:
            print(list_of_chars[x].upper(), end="")
        else:
            print("-" + list_of_chars[x].upper(), end="")
            
        n += 1
        for i in range(n):
            print(list_of_chars[x].lower(), end="")
                
    return seperate_list
    
```
```
def unique_in_order(iterable):
    new_list = []
    previous = ""
    for i in str(iterable.split()):
        if i != previous:
            new_list.append(i)
        previous = i
    new_list.remove("'")
    new_list.remove("'")
    new_list.remove("]")
    new_list.remove("[")
    return new_list



print(unique_in_order("AABBCCDD"))
```

There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.
```
def number(bus_stops):
    final = 0
    for x in bus_stops:
        final += x[0]
        final -= x[1]
    return final
```

