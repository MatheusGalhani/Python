# Python
Repositório para cadastrar exemplos de Python para treinamentos

[Feedback Treinamento](https://forms.gle/ZarFEYWqgc37XyPZ9)

Basic summary of Python operators, assignment instructions, data types and existing methods.
This tutorial is based on the tutorial on Python provided by Mosh Hamedani on YouTube.


## operators

|operator|description|
|---|---|
|+|add|
|-|subtract|
|*|multiply|
|/|float divide|
|//|integer divide|
|%|modulo|
|**|power|

there is no ++, -- in Python

## logical operators

|operator|description|
|---|---|
|==|equal|
|!=|not equal|
|>|greater than|
|<|lower than|
|>=|greater or equal|
|<=|lower or equal|
|and| logical and|
|or|logical or|
|not|logical not|


## assignments

|symbol|description|
|---|---|
|=|simple assignment x = 1 or x, y = 1, 2 or x = y = 1|
|+=|add and assign|
|-=|subtract and assign|
|*=|multiply and assign|
|/=|float divide and assign|
|//=|integer devide and assign|
|%=|modulo and assign|
|**=|power and assign|


## escape sequences

|escape sequence|result|
|---|---|
|\\"|"|
|\\'|'|
|\\\\ |\\ |
|\\n|line feed|
|\\r|carriage return|
|\\t|tab|


## types

types are classes in Python

|type|description|
|---|---|
|bool|boolean: False True with uppercase|
|float|float: 1.1|
|int|integer: 1 2 1000|
|list|array of values [1, 2, 3]|
|range|range(firstValue, lastValue, step)|
|str|string: "something" or """multilines string"""|
|tuple|(number, other_number) editable array|

variable types are defined by setting a value, however we may handled typed variables with the mypy linter module:

integers are immutable, i.e. there value cannot change, hence a new memory location is redefined each time the value is changed.

### immutable types

+ bool
+ int
+ str

### mutable types

+ list

### type annotation

``` python
x: int = 1
x = "something" # throws an error with mypy linter

x = 1000
print(type(x)) # returns <class 'int'>
```

### strings

the \\ is used as escape character  
instead of using a sequence of \n in a string it is better to use """

``` python
message = 'this is a "string with quotes"'
print(message)  # returns this is a "string with quotes"
message = "this is a \"string with quotes\""
print(message)  # returns this is a "string with quotes"
message = """this is a 
2 lines text"""
```

to format a string prefix the " with a f char  
the formatting consists in putting variable names or any valid expression between { } brackets, they'll be replaced with the value at run time

``` python
text1 = "text 1"
text2 = "text 2"
text3 = text1 + " " + text2  # usual concatenation
print(text3)  # returns text1 text2
text3 = f"   {text1} {text2}   "  # better way of formatting
print(text3)  # same output as before
print(text3.upper())  # UPPER CASE
print(text3.title())  # Proper Case
print(text3.replace("t", "_"))  # replaces all t chars with _
print("text" in text3)  # returns True if text is found in text3
print("text" not in text3)  # returns False, inverse of the above
print(text3.find("text 2"))  # returns 10
print(text3.find("Text 2"))  # returns -1, find is case sensitve
print(text3.strip())  # trim leading and trailing spaces
text4 = f"{len(text1)}, {len(text2)}"  # expressions between {}
print(text4)
```

output

```
text 1 text 2
   text 1 text 2   
   TEXT 1 TEXT 2   
   Text 1 Text 2   
   _ex_ 1 _ex_ 2   
True
False
10
-1
text 1 text 2
6, 6
```

### numbers

``` python
x = 10

x = 0b10  # binary representation of decimal 2
print(x)
print(bin(x))

x=0x12c  # hexadecimal representation of 300
print(x)
print(hex(x))
print(bin(x))

# complex numbers
y = 2 + 3j # j is the imaginary number
print(y)
```

output

```
2
0b10
300
0x12c
0b100101100
(2+3j)
```

### list / array

to access an item in a list use the [] notation.  
negative indexes are allowed, they return values from right to left  
the second index indicates where the sequence should stop, i.e. the returned value will be from first index to second index-1

``` python
sentence = "a text sample"
print(sentence[2])) # returns t
print(sentence[-2])) # returns l
print(sentence[2:8])  # returns text s
print(sentence[:4])  # is equivalent to sentence[0:4]
print(sentence[4:]) # returns from the 4 character to the end xt sample

a = [1, 2, 3]
a.append(4)  # appends the value 4to the list
```


## built-in functions

|||**built-in functions**|||
|---|---|---|---|---|
|abs()|delattr()|hash()|memoryview()|set()|
|all()|dict()|help()|min()|setattr()|
|any()|dir()|hex()|next()|slice()|
|ascii()|divmod()|id()|object()|sorted()|
|bin()|enumerate()|input()|oct()|staticmethod()|
|bool()|eval()|int()|open()|str()|
|breakpoint()|exec()|isinstance()|ord()|sum()|
|bytearray()|filter()|issubclass()|pow()|super()|
|bytes()|float()|iter()|print()|tuple()|
|callable()|format()|len()|property()|type()|
|chr()|frozenset()|list()|range()|vars()|
|classmethod()|getattr()|locals()|repr()|zip()|
|compile()|globals()|map()|reversed()|\_\_import\_\_()|
|complex()|hasattr()|max()|round()| |

### few functions described

|function|description|
|---|---|
|bin|bin(x) converts to binary|
|hex|hex(x) converts to hexadecimal|
|id|id(x) returns the memory location of variable x|
|len|len(my_var) returns the number of items in my_var|
|print|print(x) displays the value to the console you may also use print("*" * 10) to print 10 times the * char|
|round|round(x) round a float to the closest integer|
|type|type(x) returns the variable type|


## math module

``` python
import math

PI = -3.14
print(round(PI))
print(abs(PI))
print(math.floor(PI))
print(math.ceil(PI))
print(math.cos(PI/3))
```

output

```
-3
3.14
-4
-3
0.5004596890082058
```

## statements

``` python
age = 18

if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("kid")

name = "Olivier"

if not name:
    print("name is emptty")
else:
    print(f"name is {name}")

age = 22

if age >= 18 and age < 65:
    print("eligible")
else:
    print("not elligible")

# a better way to write it
if 18 <= age < 65:
    print("eligible")
else:
    print("not eligible")

# equivalent to the C syntax message = 18 <= age < 65 ? "eligible" : "not eligible"
message = "eligible" if 18 <= age < 65 else "not eligible"
print(message)
```

output

```
adult
name is Olivier
elligible
elligible
elligible
```

## loops

There are 2 types of loops in Python: for loops and while loops

### for loop

``` python
for x in "Olivier":
    print(x)

print()

for x in ["text1", "test2", "text3"]:
    print(x)
print()

for n in range(5):
    print(n)

print()

for n in range(2, 5):
    print(n)

print()

# range 3 to 9 with step 2
for n in range(3, 10, 2):
    print(n)

print()

names = ["Olivier", "Eric"]

for name in names:
    if name.startswith("E"):
        print("found")
        break
else:
    print("not found")
```

output

```
O
l
i
v
i
e
r

text1
test2
text3

0
1
2
3
4

2
3
4

3
5
7
9

found
```

### while loop

``` python
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    # this code is executed if the loop is not interrupted using a break statement
    print("wonderful!")
```

```
Guess: 1
Guess: 5
wonderful!
```


## functions

``` python
def increment(number, by):
    return number + by


print(increment(2, 3))
```
output

```
5
```

a better way to write this function

``` python
def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, by=3))
```
output

```
(2, 5)
```

when a parameter is prefixed with * it becomes a tuple,  
this provides the ability to pass an arbitrary number of arguments to a function

``` python
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
```

output

```
120
```

when a parameter is prefixed with a double * character, the arguments are passed as keyword arguments,  
i.e. parameterName=value value pairs

``` python
def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=1, name="Olivier")
```

user is similar to a javascript object

```
{'id': 1, 'name': 'Olivier'}
1
Olivier
```

## classes

``` python
class Employee:
	# __init__ is the constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com".lower()
    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("Olivier", "Brun", 5000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1)
print(emp_2)
print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())
```

output

```
<__main__.Employee object at 0x000001E5D5E606D8>
<__main__.Employee object at 0x000001E5D5E60710>
olivier.brun@company.com
test.user@company.com
Test User
```

### class methods vs instance methods and alternate constructor

``` python
import datetime


class Employee:
    number_of_emps = 0
    raise_amount = 1.04

    # those are instance methods
    # __init__ is the constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com".lower()
        Employee.number_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # this is a class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # alternative constructor when the argument is passed as a string with a dash delimiter
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    # this is a static method embedded in the class
    @staticmethod
    def is_workday(day):
        return not(day.weekday() == 5 or day.weekday() == 6)


emp_1 = Employee("Olivier", "Brun", 50000)
emp_2 = Employee("Test", "User", 60000)
emp_3 = Employee.from_string("Test2-User2-70000")
print(emp_1)
print(emp_2)
print(f"number of employess: {Employee.number_of_emps}")
print(f"empl_1 email: {emp_1.email}")
print(f"empl_2 email: {emp_2.email}")
print(f"empl_2 full name: {emp_2.fullname()}")
print(f"emp_1 pay: {emp_1.pay}")
print(
    f"emp_3 full name: {emp_3.fullname()}, emp_3 email: {emp_3.email}, emp_3 pay: {emp_3.pay}")
emp_1.apply_raise()
print(f"emp_1 raised pay: {emp_1.pay}")
emp_3.apply_raise()
print(f"emp_3 raised pay: {emp_3.pay}")

my_date = datetime.date(2018, 12, 3)
print(Employee.is_workday(my_date))
```

output

```
<__main__.Employee object at 0x0000021FD3430940>
<__main__.Employee object at 0x0000021FD3430AC8>
number of employess: 3
empl_1 email: olivier.brun@company.com
empl_2 email: test.user@company.com
empl_2 full name: Test User
emp_1 pay: 50000
emp_3 full name: Test2 User2, emp_3 email: test2.user2@company.com, emp_3 pay: 70000
emp_1 raised pay: 52000
emp_3 raised pay: 72800
True
```
