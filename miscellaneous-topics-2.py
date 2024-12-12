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
for i in range(1,500):
    s=str(i)
    if s==s[::-1]:
        print(s)

## Example 2
birthday = 'January 1, 2003'
year = int(birthday[-4:])
print('You are', 2024-year, 'years old.')

## Example 3
## By for loop.

num=(39)
digit = str(num)
answer = 0
for i in range(len(digit)):
    answer = answer + int(digit[i])
print(answer)

## By List comprehension.
num=(19)
answer = sum([int(c) for c in str(num)])
print(answer)


## if game_over:           ==       if game_over==True:   Booleans
## while not game_over:    ==       while game_over==False:   Booleans
