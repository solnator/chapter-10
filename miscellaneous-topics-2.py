### str is used to convert things into string.

## Statement       Result
## str(37)         '37'
## str(3.14)       '3.14'
## str([1,2,3])    '[1,2,3]

### int function converts something into integers.
### float function converts something into floating point number.

## Statement      Result
## int('37')       37
## float('3.14')   3.14
## int(3.14)       3
# list(range(5))   [0,1,2,3,4]
# list('abc')      ['a','b','c']

## Example 1:find palindromic numbers.
for i in range(1, 500):
    s = str(i)
    if s == s[::-1]:
        print(s)

## Example 2
birthday = "January 1, 2003"
year = int(birthday[-4:])
print("You are", 2024 - year, "years old.")

## Example 3
## By for loop.

num = 39
digit = str(num)
answer = 0
for i in range(len(digit)):
    answer = answer + int(digit[i])
print(answer)

## By List comprehension.
num = 19
answer = sum([int(c) for c in str(num)])
print(answer)

"""
### 10.2 Booleans
Are basic data type in programming represents by two possible values: True or False
"""
## if game_over:           ==       if game_over==True:
## while not game_over:    ==       while game_over==False:


### 10.3 Shortcuts
# Statement         Shorthand
# count=count+1      count+=1
# total=total-5      total-=5
# prod=prod*2        prod*=2
## There are also shortcut operators /=, %=, //=, and **=.
# a=0
# b=0      it's shortcut a=b=c=0
# c=0

# num=(10,20,30,40,50)
# a=num[0]=10
# b=num[1]=20
# c=num[2]=30  its shortcut is   a,b,c,d,e=1,2,3,4,5
# d=num[3]=40
# e=num[4]=50

## Shortcut with conditions.
# Statement                              Shortcut
# if a==0 and b==0 and c==0:             if a==b==c==0:
# if 1<a and a<b and b<5:                if 1<a<b<5:

### 10.5 Continuation(\)
string = input("Enter string.")
if "a" in string or "e" in string or "i" in string or "o" in string or "u" in string:
    print("You use 'Vowel' letter.")

### 10.7 String formatting
### Formatting Floats(:f)

a = 23.60 * 0.25
print("The tip is {:.2f}".format(a))

bill = 23.60
tip = 23.60 * 0.25
print("Tip: ${:.2f}, Total: ${:.2f}".format(tip, bill + tip))

### formatting integers(:d)
print("{:4d}".format(2))
print("{:4d}".format(20))
print("{:4d}".format(200))
print("{:4d}".format(2000))

print("{:^9d}".format(2))
print("{:^9d}".format(200))
print("{:^9d}".format(20000))
print("{:^9d}".format(2000000))
print("{:^9d}".format(200000000))

print("{:,d}".format(200000000))  # Separet by comma(,)


### Formatting Strings(:s)
print("{:^9s}".format("E"))  # Center-align
print("{:>9s}".format("hey"))  # Left-align
print("{:<9s}".format("solomon"))  # Right-align


### 10.8 Nested Loops
### Multiplication teble (10*10)
for i in range(1, 11):
    for j in range(1, 11):
        print("{:2d}".format(i * j), end=" ")
print()


### Nested loop with three (3) loops
# Outer loop
for i in range(2):  # Represents "layer"
    print(f"Layer {i+1}:")
    # Middle loop
    for j in range(3):  # Represents "row"
        # Inner loop
        for k in range(4):  # Represents "column"
            print(f"({i}, {j}, {k})", end=" ")  # Print each coordinate
        print()  # Move to the next row
    print()  # Separate each layer

### Example 2
for x in range(-50, 51):  # Outer loop for x
    for y in range(-50, 51):  # Inner loop for y
        if 2 * x + 3 * y == 4 and x - y == 7:  # Check if both equations are satisfied
            print(f"Solution:x={x},y={y}")


# ### Example 3
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            if x**2 + y**2 == z**2:
                print(f"x={x}  y={y}  z={z}")


for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            if x**2 + y**2 == z**2:
                for i in range(2, x):
                    if x % i == 0 and y % i == 0 and z % i == 0:
                        break
                else:
                    print((x, y, z), end=" ")
